/**
 * Cloudflare Pages Function: /api/submit
 * Handles form submissions from all three website forms:
 * 1. consultation-modal (Consultation Modal dialog on all pages)
 * 2. contact-page (/contact-us/)
 * 3. consultation-page (/consultation/ standalone page)
 *
 * Sequence:
 * 1. Validate inputs, origin, size & honeypot spam traps.
 * 2. Save submission permanently to Cloudflare D1 (FORM_DB binding).
 * 3. Attempt email dispatch to Gmail via Cloudflare Email Sending REST API.
 * 4. Update email delivery status in D1.
 * 5. Return JSON response to client.
 */

// Helper to escape HTML characters in email bodies to prevent injection
function escapeHtml(str) {
  if (typeof str !== 'string') return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// CORS helper headers
function getCorsHeaders(request) {
  const origin = request.headers.get('Origin') || '';
  const allowedOrigins = [
    'https://smaranraut.com.np',
    'http://smaranraut.com.np',
    'https://www.smaranraut.com.np',
    'https://smaran-raut.pages.dev'
  ];

  let allowOrigin = 'https://smaranraut.com.np';
  if (allowedOrigins.includes(origin) || origin.endsWith('.smaran-raut.pages.dev') || origin.startsWith('http://localhost:') || origin.startsWith('http://127.0.0.1:')) {
    allowOrigin = origin;
  }

  return {
    'Access-Control-Allow-Origin': allowOrigin,
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin'
  };
}

// Handle OPTIONS preflight
export async function onRequestOptions(context) {
  return new Response(null, {
    status: 204,
    headers: getCorsHeaders(context.request)
  });
}

// Handle GET requests (safe status/health check without leaking data)
export async function onRequestGet(context) {
  const corsHeaders = getCorsHeaders(context.request);
  const url = new URL(context.request.url);

  // Simple readiness verification endpoint: /api/submit?check=1
  if (url.searchParams.get('check') === '1') {
    let dbStatus = 'disconnected';
    let submissionCount = 0;

    if (context.env && context.env.FORM_DB) {
      try {
        await ensureTableExists(context.env.FORM_DB);
        const result = await context.env.FORM_DB.prepare('SELECT COUNT(*) as count FROM form_submissions').first();
        dbStatus = 'connected';
        submissionCount = result ? result.count : 0;
      } catch (e) {
        dbStatus = 'error: ' + (e.message || String(e));
      }
    }

    const emailConfigured = Boolean(context.env && context.env.CLOUDFLARE_EMAIL_API_TOKEN);

    return new Response(JSON.stringify({
      status: 'ready',
      endpoint: '/api/submit',
      database_binding: 'FORM_DB',
      database_status: dbStatus,
      total_submissions: submissionCount,
      email_sending_configured: emailConfigured,
      timestamp: new Date().toISOString()
    }, null, 2), {
      status: 200,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  return new Response(JSON.stringify({
    error: 'Method Not Allowed',
    message: 'This endpoint accepts POST form submissions. Use ?check=1 for diagnostic status.'
  }), {
    status: 405,
    headers: { ...corsHeaders, 'Content-Type': 'application/json', 'Allow': 'POST, GET, OPTIONS' }
  });
}

// Ensure the D1 database table and indexes exist
async function ensureTableExists(db) {
  await db.prepare(`
    CREATE TABLE IF NOT EXISTS form_submissions (
      id TEXT PRIMARY KEY,
      form_type TEXT NOT NULL,
      page_url TEXT,
      name TEXT,
      email TEXT,
      phone TEXT,
      submitted_data TEXT NOT NULL,
      submitted_at TEXT NOT NULL,
      email_status TEXT NOT NULL DEFAULT 'pending',
      email_message_id TEXT,
      email_error TEXT,
      ip_address TEXT,
      user_agent TEXT
    );
  `).run();

  // Create indexes if not exist
  await db.prepare(`CREATE INDEX IF NOT EXISTS idx_form_submissions_type ON form_submissions(form_type);`).run();
  await db.prepare(`CREATE INDEX IF NOT EXISTS idx_form_submissions_date ON form_submissions(submitted_at);`).run();
}

// Handle POST submissions
export async function onRequestPost(context) {
  const { request, env } = context;
  const corsHeaders = getCorsHeaders(request);

  // 1. Payload size protection (max 100 KB)
  const contentLength = request.headers.get('content-length');
  if (contentLength && parseInt(contentLength, 10) > 102400) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Payload too large. Maximum size is 100 KB.'
    }), {
      status: 413,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  // 2. Parse request body (JSON or Form URL-Encoded / FormData)
  let rawData = {};
  const contentType = (request.headers.get('content-type') || '').toLowerCase();

  try {
    if (contentType.includes('application/json')) {
      rawData = await request.json();
    } else if (contentType.includes('application/x-www-form-urlencoded') || contentType.includes('multipart/form-data')) {
      const formData = await request.formData();
      for (const [key, value] of formData.entries()) {
        rawData[key] = value;
      }
    } else {
      // Fallback: try json, then text
      const text = await request.text();
      try {
        rawData = JSON.parse(text);
      } catch {
        const params = new URLSearchParams(text);
        for (const [key, value] of params.entries()) {
          rawData[key] = value;
        }
      }
    }
  } catch (err) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Invalid request data format.'
    }), {
      status: 400,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  // 3. Honeypot Spam Protection
  // If "bot-field" has content, silently discard and respond with success
  if (rawData['bot-field'] || rawData['bot_field']) {
    return new Response(JSON.stringify({
      success: true,
      message: 'Submission received.'
    }), {
      status: 200,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  // 4. Form Identification & Mapping
  // Check form identifier
  const formNameInput = (rawData['form-name'] || rawData['form_type'] || rawData['form_name'] || rawData['formId'] || '').trim().toLowerCase();

  let formType = '';
  let formDisplayName = '';

  if (formNameInput === 'consultation-modal' || formNameInput === 'consultation-form' || formNameInput === 'consultation') {
    formType = 'consultation-modal';
    formDisplayName = 'Consultation Modal Request';
  } else if (formNameInput === 'contact-page' || formNameInput === 'contact-page-form' || formNameInput === 'contact') {
    formType = 'contact-page';
    formDisplayName = 'Contact Us Page Message';
  } else if (formNameInput === 'consultation-page' || formNameInput === 'standalone-consultation-form' || formNameInput === 'consultation-page-form') {
    formType = 'consultation-page';
    formDisplayName = 'Standalone Consultation Booking';
  } else {
    // Attempt automatic detection from distinct field keys
    if (rawData.client_name || rawData.client_email || rawData.service_interest) {
      formType = 'consultation-modal';
      formDisplayName = 'Consultation Modal Request';
    } else if (rawData.message) {
      formType = 'contact-page';
      formDisplayName = 'Contact Us Page Message';
    } else if (rawData.focus) {
      formType = 'consultation-page';
      formDisplayName = 'Standalone Consultation Booking';
    } else {
      return new Response(JSON.stringify({
        success: false,
        error: 'Unrecognized form identifier. Please specify form-name.'
      }), {
        status: 400,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
  }

  // 5. Extract and normalize fields across the 3 forms
  const name = String(rawData.client_name || rawData.name || '').trim();
  const email = String(rawData.client_email || rawData.email || '').trim().toLowerCase();
  const phone = String(rawData.client_phone || rawData.phone || '').trim();
  const website = String(rawData.client_website || rawData.website || '').trim();
  const serviceOrFocus = String(rawData.service_interest || rawData.focus || '').trim();
  const notesOrMessage = String(rawData.client_notes || rawData.message || '').trim();
  const pageUrl = String(rawData.page_url || request.headers.get('Referer') || 'https://smaranraut.com.np').trim();

  // 6. Server-Side Validation
  if (!name || name.length > 150) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Please provide a valid full name (maximum 150 characters).'
    }), {
      status: 400,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email || !emailRegex.test(email) || email.length > 254) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Please provide a valid email address.'
    }), {
      status: 400,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  if (!phone || phone.length < 5 || phone.length > 50) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Please provide a valid contact phone or WhatsApp number.'
    }), {
      status: 400,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  if (website && website.length > 300) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Website URL exceeds the maximum allowed length (300 characters).'
    }), {
      status: 400,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  if (notesOrMessage && notesOrMessage.length > 5000) {
    return new Response(JSON.stringify({
      success: false,
      error: 'Message or notes text exceeds the maximum allowed length (5000 characters).'
    }), {
      status: 400,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  // 7. Metadata Generation
  const submissionId = 'sub_' + crypto.randomUUID().replace(/-/g, '');
  const submittedAt = new Date().toISOString();
  const clientIp = request.headers.get('CF-Connecting-IP') || 'unknown';
  const userAgent = request.headers.get('User-Agent') || 'unknown';

  // Construct structured submission payload (clean of internal tokens)
  const cleanSubmittedData = {
    form_type: formType,
    form_display_name: formDisplayName,
    name,
    email,
    phone,
    website: website || null,
    service_or_focus: serviceOrFocus || null,
    message_or_notes: notesOrMessage || null,
    page_url: pageUrl,
    submitted_at: submittedAt,
    client_ip: clientIp,
    raw_fields: rawData
  };
  const submittedDataJson = JSON.stringify(cleanSubmittedData);

  // 8. Step 1: Save Submission to Cloudflare D1
  if (!env || !env.FORM_DB) {
    console.error('CRITICAL: FORM_DB D1 binding is not defined on context.env');
    return new Response(JSON.stringify({
      success: false,
      error: 'Database service configuration is missing. Please contact us directly at contact@smaranraut.com.np.'
    }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  try {
    await ensureTableExists(env.FORM_DB);

    await env.FORM_DB.prepare(`
      INSERT INTO form_submissions (
        id, form_type, page_url, name, email, phone,
        submitted_data, submitted_at, email_status, ip_address, user_agent
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)
    `).bind(
      submissionId,
      formType,
      pageUrl,
      name,
      email,
      phone,
      submittedDataJson,
      submittedAt,
      clientIp,
      userAgent
    ).run();

  } catch (dbError) {
    console.error('D1 Storage Failed:', dbError);
    return new Response(JSON.stringify({
      success: false,
      error: 'We were unable to record your submission due to a database error. Please try again or reach out directly.'
    }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  // 9. Step 2: Attempt Email Notification via Cloudflare Email Sending REST API
  // Configuration lookup
  const accountId = (env.CLOUDFLARE_ACCOUNT_ID || '85f591f6a7975bcf428709ad916955c1').trim();
  const emailApiToken = (env.CLOUDFLARE_EMAIL_API_TOKEN || '').trim();
  const toEmail = (env.FORMS_TO_EMAIL || 'playzswifty05@gmail.com').trim();
  const fromEmail = (env.FORMS_FROM_EMAIL || 'contact@smaranraut.com.np').trim();

  let emailStatus = 'pending';
  let emailMessageId = null;
  let emailError = null;

  if (!emailApiToken) {
    emailStatus = 'unconfigured';
    emailError = 'CLOUDFLARE_EMAIL_API_TOKEN environment secret is not set.';
    console.warn(emailError);
  } else {
    // Construct Email Content
    const emailSubject = `[Website Lead] ${formDisplayName}: ${name}`;
    
    const plainTextContent = `New Form Submission Received
-------------------------------------------
Submission ID: ${submissionId}
Form: ${formDisplayName} (${formType})
Submitted At: ${submittedAt} UTC
Page URL: ${pageUrl}

Visitor Information:
- Full Name: ${name}
- Email: ${email}
- Phone / WhatsApp: ${phone}
${website ? `- Website: ${website}\n` : ''}${serviceOrFocus ? `- Service / Package: ${serviceOrFocus}\n` : ''}
${notesOrMessage ? `Message / Project Details:\n${notesOrMessage}\n` : ''}
-------------------------------------------
Client IP: ${clientIp}
Saved in Cloudflare D1 Database (ID: ${submissionId})
`;

    const htmlContent = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f6f5; margin: 0; padding: 24px; color: #1e293b; }
    .card { max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
    .header { background-color: #245037; color: #ffffff; padding: 20px 24px; }
    .header h1 { margin: 0; font-size: 1.25rem; font-weight: 600; letter-spacing: -0.01em; }
    .header p { margin: 4px 0 0 0; opacity: 0.85; font-size: 0.85rem; }
    .body { padding: 24px; }
    .field-group { margin-bottom: 16px; }
    .label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; font-weight: 600; margin-bottom: 4px; }
    .value { font-size: 0.95rem; color: #0f172a; line-height: 1.5; }
    .message-box { background: #f8fafc; border-left: 3px solid #8F6B38; padding: 12px 16px; border-radius: 0 4px 4px 0; font-size: 0.95rem; white-space: pre-wrap; }
    .badge { display: inline-block; padding: 3px 8px; background: #e0ece4; color: #245037; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }
    .footer { background: #f8fafc; border-top: 1px solid #e2e8f0; padding: 14px 24px; font-size: 0.75rem; color: #64748b; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h1>New Website Lead</h1>
      <p>${escapeHtml(formDisplayName)} &bull; ${escapeHtml(submittedAt)}</p>
    </div>
    <div class="body">
      <div class="field-group">
        <span class="badge">${escapeHtml(formType)}</span>
      </div>
      <div class="field-group">
        <div class="label">Full Name</div>
        <div class="value"><strong>${escapeHtml(name)}</strong></div>
      </div>
      <div class="field-group">
        <div class="label">Email Address</div>
        <div class="value"><a href="mailto:${escapeHtml(email)}" style="color: #245037;">${escapeHtml(email)}</a></div>
      </div>
      <div class="field-group">
        <div class="label">Phone / WhatsApp Number</div>
        <div class="value"><a href="tel:${escapeHtml(phone)}" style="color: #245037;">${escapeHtml(phone)}</a></div>
      </div>
      ${website ? `
      <div class="field-group">
        <div class="label">Current Website</div>
        <div class="value"><a href="${escapeHtml(website)}" target="_blank" rel="noopener">${escapeHtml(website)}</a></div>
      </div>` : ''}
      ${serviceOrFocus ? `
      <div class="field-group">
        <div class="label">Requested Service / Package</div>
        <div class="value">${escapeHtml(serviceOrFocus)}</div>
      </div>` : ''}
      ${notesOrMessage ? `
      <div class="field-group">
        <div class="label">Project Notes / Message</div>
        <div class="message-box">${escapeHtml(notesOrMessage)}</div>
      </div>` : ''}
      <div class="field-group" style="margin-top: 20px; border-top: 1px dashed #e2e8f0; padding-top: 12px;">
        <div class="label">Originating Page</div>
        <div class="value" style="font-size: 0.8rem; word-break: break-all;"><a href="${escapeHtml(pageUrl)}">${escapeHtml(pageUrl)}</a></div>
      </div>
    </div>
    <div class="footer">
      Submission ID: <code>${escapeHtml(submissionId)}</code> &bull; Saved in Cloudflare D1
    </div>
  </div>
</body>
</html>
`;

    try {
      const emailEndpoint = `https://api.cloudflare.com/client/v4/accounts/${accountId}/email/sending/send`;
      
      const emailPayload = {
        to: [toEmail],
        from: {
          address: fromEmail,
          name: "Smaran Raut Portfolio"
        },
        reply_to: email,
        subject: emailSubject,
        content: [
          { type: "text/plain", value: plainTextContent },
          { type: "text/html", value: htmlContent }
        ]
      };

      const emailResponse = await fetch(emailEndpoint, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${emailApiToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(emailPayload)
      });

      const emailResult = await emailResponse.json().catch(() => ({}));

      if (emailResponse.ok && emailResult.success) {
        emailStatus = 'sent';
        emailMessageId = (emailResult.result && emailResult.result.id) ? String(emailResult.result.id) : 'delivered';
      } else {
        emailStatus = 'failed';
        emailError = `HTTP ${emailResponse.status}: ${JSON.stringify(emailResult.errors || emailResult.messages || emailResult)}`;
        console.warn('Cloudflare Email Sending rejected request:', emailError);
      }
    } catch (err) {
      emailStatus = 'failed';
      emailError = err.message || String(err);
      console.error('Email dispatch threw exception:', err);
    }
  }

  // 10. Update D1 submission with email delivery status
  try {
    await env.FORM_DB.prepare(`
      UPDATE form_submissions
      SET email_status = ?, email_message_id = ?, email_error = ?
      WHERE id = ?
    `).bind(
      emailStatus,
      emailMessageId,
      emailError,
      submissionId
    ).run();
  } catch (updateErr) {
    console.error('Failed to update email status in D1:', updateErr);
  }

  // 11. Return Success Response to User
  // Since the submission is securely preserved in D1, inform user of success
  return new Response(JSON.stringify({
    success: true,
    submission_id: submissionId,
    message: `Thank you, ${name}! Your inquiry has been securely received by Smaran Raut. We will contact you within 24 business hours.`,
    email_status: emailStatus
  }), {
    status: 200,
    headers: { ...corsHeaders, 'Content-Type': 'application/json' }
  });
}
