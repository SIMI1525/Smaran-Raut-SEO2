# Apply Algorithmic Authorship and Supplementary Internal Linking SOP
import os

html_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\top-seo-experts-in-nepal\index.html"
wp_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\top-seo-experts-in-nepal.php"
blog_index_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html"
page_blog_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\page-blog.php"
header_wp_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\header.php"

# 9 Verified Professionals
professionals = [
    {
        "num": "1",
        "name": "Smaran Raut",
        "title": "Web Developer & SEO Expert",
        "location": "Itahari, Nepal",
        "company": None,
        "skills": ["Website Development", "Local SEO", "Technical Audits", "Keyword Research", "Content Optimisation", "GBP Optimisation"],
        "website": "https://smaranraut.com.np/",
        "gbp": "https://g.page/r/CXbkZaR8nj4kEBM/review",
        "gbp_label": "Verified Listing"
    },
    {
        "num": "2",
        "name": "Krishna Bogati",
        "title": "SEO Expert & WordPress Specialist",
        "location": "Kathmandu, Nepal",
        "company": None,
        "skills": ["Technical SEO", "WordPress Tuning", "On-Page SEO", "AI Search Strategy"],
        "website": "https://krishnabogati.com.np/",
        "gbp": None,
        "gbp_label": "Unavailable"
    },
    {
        "num": "3",
        "name": "Ujjwal Rupakheti",
        "title": "Web Developer & SEO Specialist",
        "location": "Itahari, Nepal",
        "company": None,
        "skills": ["Website Development", "Technical SEO", "Local SEO", "Core Web Vitals"],
        "website": "https://www.ujjwalrupakheti.com.np/",
        "gbp": None,
        "gbp_label": "Unavailable"
    },
    {
        "num": "4",
        "name": "Sushant Karn",
        "title": "SEO Consultant & Growth Specialist",
        "location": "Kathmandu, Nepal",
        "company": None,
        "skills": ["SEO Consulting", "Technical Diagnostics", "Link Building", "Content Strategy"],
        "website": "https://sushantkarn.info.np/",
        "gbp": None,
        "gbp_label": "Unavailable"
    },
    {
        "num": "5",
        "name": "Suman Dhami",
        "title": "SEO Expert & Web Developer",
        "location": "Kathmandu, Nepal",
        "company": "AlpineRoot",
        "skills": ["Technical SEO Audits", "Ongoing SEO Campaigns", "Cross-Border SEO", "Custom Web Development"],
        "website": "https://sumandhami.com.np/",
        "gbp": None,
        "gbp_label": "Unavailable"
    },
    {
        "num": "6",
        "name": "Diwakar Bhatt",
        "title": "SEO Specialist & Web Developer",
        "location": "Kathmandu, Nepal",
        "company": None,
        "skills": ["Crawl Architecture", "Structured Data (Schema)", "Answer Engine Optimisation", "Keyword Research"],
        "website": "https://diwakarbhatt.com.np/",
        "gbp": None,
        "gbp_label": "Unavailable"
    },
    {
        "num": "7",
        "name": "Suraj Giri",
        "title": "Independent SEO Consultant",
        "location": "Bhaktapur, Nepal",
        "company": None,
        "skills": ["Independent SEO Consulting", "Technical Diagnostics", "Local Maps Placement", "SEO Training"],
        "website": "https://seoexpertinnepal.com/",
        "gbp": "https://maps.google.com/?cid=12380517030472402827",
        "gbp_label": "Verified Listing"
    },
    {
        "num": "8",
        "name": "Dipak Paneru",
        "title": "Digital Marketing & Technical SEO Specialist",
        "location": "Nepal (Global Consultant)",
        "company": None,
        "skills": ["Local SEO & Map Pack", "Technical Entity SEO", "Multi-Region Search", "Digital Marketing"],
        "website": "https://dipakpaneru.com/",
        "gbp": "https://g.page/r/CYU3MsvIRvvTEBM/review",
        "gbp_label": "Verified Listing"
    },
    {
        "num": "9",
        "name": "Rahul Ranjan",
        "title": "SEO Expert & Full Stack Developer",
        "location": "Biratnagar, Nepal",
        "company": None,
        "skills": ["Next.js & Technical SEO", "Full Stack Development", "GA4 Measurement", "Lead Generation"],
        "website": "https://www.rahulranjan.com.np/",
        "gbp": None,
        "gbp_label": "Unavailable"
    }
]

def render_table_rows():
    rows = []
    for p in professionals:
        company_tag = f' <span class="table-company-badge">{p["company"]}</span>' if p["company"] else ''
        skills_html = ' &middot; '.join(p["skills"])
        web_link = f'<a href="{p["website"]}" target="_blank" rel="noopener noreferrer" class="tbl-link tbl-link--web">Visit Website <span class="arr">&nearr;</span></a>'
        if p["gbp"]:
            gbp_cell = f'<a href="{p["gbp"]}" target="_blank" rel="noopener noreferrer" class="tbl-link tbl-link--gbp">Verified Profile <span class="arr">&nearr;</span></a>'
        else:
            gbp_cell = '<span class="tbl-dim">&mdash;</span>'
            
        row = f'''          <tr class="dir-row" data-search="{p["name"].lower()} {p["location"].lower()} {" ".join(p["skills"]).lower()}">
            <td class="col-num">{p["num"]}</td>
            <td class="col-name">
              <div class="name-text">{p["name"]}{company_tag}</div>
              <div class="title-sub">{p["title"]}</div>
            </td>
            <td class="col-loc">{p["location"]}</td>
            <td class="col-exp">{skills_html}</td>
            <td class="col-web">{web_link}</td>
            <td class="col-gbp">{gbp_cell}</td>
          </tr>'''
        rows.append(row)
    return '\n'.join(rows)

table_rows_code = render_table_rows()

# Complete Algorithmic Authorship Body Content
# Rule: Opening answers H1 immediately. Definitional pattern: [Entity] is [Class] that [Differentia].
# Rule: First sentence under each H2/H3 answers the heading directly using the heading's predicate.
# Rule: Semantic triples, EAV values explicit, units on numbers, no banned patterns.
# Rule: SOP Supplementary section near the end with exact target H1/title as anchor and 5-15 word context window.

article_prose = f'''
      <!-- Document Opening & Macro Context -->
      <section class="editorial-intro-block" style="margin-bottom: 2.75rem;">
        <p class="lead-text" style="font-size: 1.15rem; line-height: 1.75; color: #0F172A; margin-bottom: 1.35rem;">
          SEO experts in Nepal are digital search specialists who analyze, restructure, and optimize websites to achieve prominent organic rankings on Google for commercial and informational queries. These professionals resolve server-side indexation barriers, optimize on-page content relevance, and configure local business signals across Nepal's primary commercial markets, including Kathmandu, Lalitpur, Pokhara, Itahari, and Biratnagar.
        </p>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #334155; margin-bottom: 1.35rem;">
          Search engine optimization generates compounding organic customer acquisition without recurring pay-per-click fees. Effective execution requires coordination across three core operational layers: server architecture, topical content authority, and local map pack visibility. When these three layers align, search engine crawlers discover, index, and rank business pages above competitors.
        </p>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #334155; margin-bottom: 2rem;">
          Selecting the appropriate specialist depends on matching a company's specific technical requirements with verified practitioner capabilities. This directory reviews nine verified SEO practitioners in Nepal who offer documented technical, local, and architectural search services.
        </p>

        <!-- Editorial Directory Transparency Policy -->
        <div class="editorial-transparency-card" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid var(--accent-teal, #245037); padding: 1.25rem 1.5rem; border-radius: 6px; margin-bottom: 2rem;">
          <div style="font-weight: 700; font-size: 1rem; color: #0F172A; margin-bottom: 0.4rem; display: flex; align-items: center; gap: 0.5rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            Directory Verification &amp; Editorial Methodology
          </div>
          <p style="margin: 0; font-size: 0.92rem; line-height: 1.6; color: #475569;">
            This reference directory compiles verified data from official practitioner domains, active portfolio repositories, verified Google Business Profile records, and public technical contributions. Inclusion is strictly editorial and non-commercial. No practitioner has paid for placement or received preferential ranking status. Professionals appear in a sequential reference format to support objective comparison of locations, technical specialisations, and published credentials.
          </p>
        </div>
      </section>

      <!-- H2: Editorial Directory Table (Forbes Style) -->
      <section class="editorial-table-section" style="margin-bottom: 3.5rem;">
        <div class="table-header-group" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">
          <div>
            <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin: 0 0 0.35rem 0;">Directory of Verified SEO Experts in Nepal</h2>
            <div style="font-size: 0.92rem; color: #64748B;">Nine verified practitioners evaluated by technical scope, location, and verified presence</div>
          </div>
          <div class="table-filter-box" style="position: relative; min-width: 280px;">
            <input type="text" id="dirSearchInput" placeholder="Filter by name, location, skill..." style="width: 100%; padding: 0.55rem 0.85rem 0.55rem 2.25rem; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.88rem; outline: none; background: #FFFFFF; color: #1E293B;">
            <svg style="position: absolute; left: 0.75rem; top: 50%; transform: translateY(-50%); color: #94A3B8; pointer-events: none;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </div>
        </div>

        <div class="table-container-responsive" style="overflow-x: auto; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <table class="editorial-dir-table" style="width: 100%; min-width: 820px; border-collapse: collapse; text-align: left; font-size: 0.92rem;">
            <thead>
              <tr style="background: #F8FAFC; border-bottom: 2px solid #E2E8F0; color: #475569; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em;">
                <th style="padding: 1rem 1.15rem; width: 45px; text-align: center;">No.</th>
                <th style="padding: 1rem 1.15rem; width: 230px;">Professional &amp; Title</th>
                <th style="padding: 1rem 1.15rem; width: 140px;">Location</th>
                <th style="padding: 1rem 1.15rem;">Primary Expertise</th>
                <th style="padding: 1rem 1.15rem; width: 135px;">Website</th>
                <th style="padding: 1rem 1.15rem; width: 145px;">Google Business Profile</th>
              </tr>
            </thead>
            <tbody id="dirTableBody">
{table_rows_code}
            </tbody>
          </table>
        </div>
        <div id="noMatchMsg" style="display: none; padding: 2rem; text-align: center; color: #64748B; background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 8px; margin-top: 1rem;">
          No professionals matched your filter query. Reset search to view all nine listings.
        </div>
      </section>

      <!-- H2: How to Choose Section (Algorithmic Rules: First sentence answers heading) -->
      <section class="guide-content-section" style="margin-bottom: 3.5rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">How to Choose an SEO Expert in Nepal</h2>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #334155; margin-bottom: 2rem;">
          Choosing an SEO expert in Nepal requires evaluating technical audit depth, local map pack proficiency, verifiable client case studies, reporting transparency, and strict adherence to Google Search Essentials. Business stakeholders should examine these five operational criteria before signing a consulting contract:
        </p>

        <div class="evaluation-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">1</span>
              Technical Audit Depth
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              A technical audit evaluates server response codes, XML sitemaps, canonical tags, and mobile rendering speeds. When an existing web property suffers from dropped rankings, conducting comprehensive <a href="../../services/technical-seo-audit/index.html">Technical SEO Audits &amp; Search Optimization</a> identifies crawling bottlenecks and resolves duplicate parameter loops before content expansion begins.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">2</span>
              Local Map Pack Optimization
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Local search in Nepal depends on Google Business Profile verification, consistent Name-Address-Phone (NAP) citations, and verified review signals. Businesses targeting regional consumers in Sunsari, Morang, and Jhapa benefit directly from specialized <a href="../../services/local-seo-itahari/index.html">Local SEO &amp; Google Business Profile Optimization in Itahari &amp; Eastern Nepal</a> to secure placement within the top-3 Google Map Pack.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">3</span>
              Verifiable Case Studies &amp; Evidence
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Documented search evidence distinguishes proven practitioners from theoretical consultants. Reliable experts provide verifiable Google Search Console performance curves, index coverage reports, and demonstrated query impression increases across competitive commercial sectors in Nepal.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">4</span>
              Transparent Business-First KPIs
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Commercial SEO tracking measures qualified inquiries, phone calls, form completions, and organic revenue rather than isolated keyword vanity ranks. Competent consultants configure Google Analytics 4 conversion events and deliver monthly reports linked directly to business performance metrics.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">5</span>
              Adherence to Google Search Essentials
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Ethical SEO strictly follows Google Search Essentials to protect domain equity. Practitioners who employ automated backlink schemes, private blog networks, or keyword-stuffed text expose client domains to algorithmic ranking suppression that requires extensive remediation to reverse.
            </p>
          </div>
        </div>
      </section>

      <!-- H2: Freelance SEO Expert vs SEO Agency (Algorithmic Comparative Pattern) -->
      <section class="guide-content-section" style="margin-bottom: 3.5rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">Freelance SEO Expert vs SEO Agency</h2>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #334155; margin-bottom: 1.75rem;">
          Comparing a freelance SEO expert with a digital agency reveals differences across five operational dimensions: communication directness, technical focus, content production capacity, cost structure, and organizational agility.
        </p>

        <div class="table-container-responsive" style="overflow-x: auto; margin-bottom: 2rem;">
          <table style="width: 100%; min-width: 680px; border-collapse: collapse; text-align: left; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; font-size: 0.92rem;">
            <thead>
              <tr style="background: #F8FAFC; border-bottom: 2px solid #E2E8F0; color: #0F172A;">
                <th style="padding: 1rem 1.25rem; font-weight: 700;">Evaluation Dimension</th>
                <th style="padding: 1rem 1.25rem; font-weight: 700;">Independent Consultant / Freelancer</th>
                <th style="padding: 1rem 1.25rem; font-weight: 700;">Digital Marketing Agency</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Communication Flow</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Direct communication with the technical specialist executing website code and content adjustments.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Communication managed through account coordinators and centralized project ticketing systems.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Technical Focus</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Specialized focus on site architecture, Core Web Vitals, indexation hygiene, and local map pack rankings.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Broad digital marketing scope combining search optimization with paid advertising, social media, and branding.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Content Production Scale</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Structured topical briefs; collaborates directly with the client's internal subject matter experts.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">High production volume delivered through dedicated in-house copywriters, editors, and graphic designers.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Cost Efficiency</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Lean overhead; consulting fees allocate directly to specialist analysis, audit execution, and technical fixes.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Higher monthly retainers required to cover administrative personnel, office overhead, and management layers.</td>
              </tr>
              <tr>
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Organizational Fit</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Small to mid-sized businesses, regional healthcare clinics, local retailers, and startups seeking agile execution.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">National corporations, banking institutions, and enterprises requiring multi-channel marketing campaigns.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- H2: Frequently Asked Questions (Extractive Answer Rules) -->
      <section class="guide-content-section" style="margin-bottom: 3.5rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">Frequently Asked Questions About SEO Experts in Nepal</h2>
        
        <div class="faq-list" style="display: flex; flex-direction: column; gap: 1.25rem;">
          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">Who are the active SEO experts in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Nine verified SEO practitioners in Nepal are documented in this directory: Smaran Raut (Web Developer &amp; SEO Expert in Itahari), Krishna Bogati (Kathmandu), Ujjwal Rupakheti (Itahari), Sushant Karn (Kathmandu), Suman Dhami (AlpineRoot), Diwakar Bhatt (Kathmandu), Suraj Giri (Bhaktapur), Dipak Paneru (Global Consultant), and Rahul Ranjan (Biratnagar).
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">What does an SEO expert do?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              An SEO expert analyzes search engine crawl logs, eliminates indexation barriers, structures schema markup, optimizes on-page content relevance, builds local Google Map Pack citations, and tracks organic conversions using Google Search Console and GA4 to increase qualified business traffic.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">How do I choose an SEO consultant in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Choose an SEO consultant in Nepal by verifying technical speed scores on their personal domain, inspecting live client case study rankings, requiring transparent monthly GA4 reporting, and ensuring strict compliance with Google Search Essentials before committing to a consulting agreement.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">How much does SEO cost in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              SEO in Nepal typically costs between NPR 15,000 and NPR 45,000 per month for ongoing local business consulting retainers. Comprehensive one-time technical audits range from NPR 20,000 to NPR 60,000, while custom eCommerce campaigns require project-specific scoping based on product catalog scale.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">How long does SEO take to produce measurable results?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              SEO in Nepal produces initial crawl frequency and query impression increases within 4 to 8 weeks after resolving technical defects. Sustainable keyword rankings and organic commercial leads typically compound across 3 to 6 months of continuous optimization. For a detailed breakdown of algorithmic evaluation cycles, read our guide on <a href="../how-seo-works/index.html">How Does SEO Work? Understanding Search Rankings in Nepal</a>.
            </p>
          </div>
        </div>
      </section>

      <!-- SOP Section: Supplementary Internal Linking (SOP Standard) -->
      <!-- Source: /blog/top-seo-experts-in-nepal/ (H1: SEO Experts in Nepal) -->
      <!-- Semantic Bridge: Readers evaluating SEO experts often discover their underlying website architecture prevents ranking, necessitating dedicated SEO-optimized web development and speed maintenance. -->
      <!-- Target 1: /services/seo-optimized-web-development/ -> H1: SEO-Optimized Website Development in Nepal -->
      <!-- Target 2: /services/core-web-vitals-speed/ -> H1: Website Speed Optimization & Technical Maintenance -->
      <section class="supplementary-linking-block" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 2rem; margin-bottom: 3.5rem;">
        <h2 style="font-size: 1.4rem; font-weight: 700; color: #0F172A; margin: 0 0 1rem 0;">When Does SEO-Optimized Website Development in Nepal Become Necessary?</h2>
        <p style="font-size: 0.96rem; line-height: 1.7; color: #475569; margin-bottom: 1.25rem;">
          Consulting an SEO specialist frequently reveals that on-page keyword adjustments cannot overcome fundamental structural flaws, bloated templates, or unoptimized server configurations. In situations where legacy platforms suffer from unfixable code bloat, investing in custom <a href="../../services/seo-optimized-web-development/index.html">SEO-Optimized Website Development in Nepal</a> establishes fast-loading static HTML structures, mobile-first layouts, and schema validation before commercial promotion begins.
        </p>
        <p style="font-size: 0.96rem; line-height: 1.7; color: #475569; margin-bottom: 1.25rem;">
          Furthermore, active business websites experiencing layout shifts or sluggish interaction delays must maintain compliance with Google's Core Web Vitals thresholds. Implementing systematic <a href="../../services/core-web-vitals-speed/index.html">Website Speed Optimization &amp; Technical Maintenance</a> ensures mobile pages consistently render under the 2.5-second Largest Contentful Paint requirement to prevent organic ranking degradation.
        </p>
        <p style="font-size: 0.96rem; line-height: 1.7; color: #475569; margin: 0;">
          To learn more about our local search methodology, review our comprehensive framework on <a href="../google-business-profile-optimization-nepal/index.html">How to Optimize Google Business Profile in Nepal</a>. You can also review verified credentials <a href="../../about-us/index.html">About Smaran Raut: SEO &amp; Web Development in Nepal</a> or <a href="../../contact-us/index.html">Get in Touch with Smaran Raut</a> to schedule a direct technical consultation.
        </p>
      </section>

      <!-- Consultation CTA Section -->
      <section class="guide-cta-section" style="background: linear-gradient(135deg, #0A1628 0%, #142240 100%); color: #FFFFFF; padding: 2.75rem 2rem; border-radius: 8px; text-align: center; margin-bottom: 2.5rem;">
        <h3 style="color: #FFFFFF; font-size: 1.55rem; font-weight: 700; margin: 0 0 0.85rem 0;">Ready to Elevate Your Website's Search Visibility?</h3>
        <p style="color: #CBD5E1; font-size: 1.02rem; max-width: 620px; margin: 0 auto 1.75rem; line-height: 1.6;">
          Whether you need a brand-new SEO-engineered website or an audit of your current digital platform, let's discuss your project goals directly.
        </p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="../../contact-us/index.html" class="btn btn-primary" style="background: #00C2CB; color: #0A1628; font-weight: 600; padding: 0.7rem 1.6rem; border-radius: 6px; text-decoration: none; border: none;">Contact Smaran Raut &rarr;</a>
          <a href="../../services/index.html" class="btn btn-outline" style="border: 1px solid #CBD5E1; color: #FFFFFF; font-weight: 600; padding: 0.7rem 1.6rem; border-radius: 6px; text-decoration: none;">View All Services</a>
        </div>
      </section>
'''

editorial_css = '''
  <style>
    /* Hero Directory Styling */
    .hero-directory {
      position: relative;
      overflow: hidden;
      padding: 4.5rem 0 3.75rem;
      background-color: #0b111a;
      background-image: linear-gradient(180deg, rgba(11, 17, 26, 0.84) 0%, rgba(11, 17, 26, 0.95) 100%), url('../../images/seo-experts-hero.jpg');
      background-size: cover;
      background-position: center;
      color: #FFFFFF;
    }
    @media (max-width: 768px) {
      .hero-directory {
        padding: 3rem 0 2.5rem;
      }
    }
    
    /* Forbes-Inspired Editorial Directory Table */
    .editorial-dir-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .editorial-dir-table th {
      background: #F8FAFC;
      color: #475569;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 2px solid #E2E8F0;
      padding: 1rem 1.15rem;
      white-space: nowrap;
    }
    .editorial-dir-table td {
      padding: 1.1rem 1.15rem;
      border-bottom: 1px solid #E2E8F0;
      vertical-align: middle;
      color: #334155;
    }
    .editorial-dir-table tr.dir-row:hover td {
      background-color: #F8FAFC;
    }
    .col-num {
      text-align: center;
      font-weight: 600;
      color: #64748B;
      font-size: 0.95rem;
      width: 45px;
    }
    .col-name .name-text {
      font-weight: 700;
      color: #0F172A;
      font-size: 1.02rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .col-name .title-sub {
      font-size: 0.84rem;
      color: #2563EB;
      font-weight: 500;
      margin-top: 0.2rem;
    }
    .table-company-badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 600;
      background: #F1F5F9;
      color: #475569;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      border: 1px solid #E2E8F0;
    }
    .col-loc {
      font-size: 0.88rem;
      color: #475569;
      white-space: nowrap;
    }
    .col-exp {
      font-size: 0.85rem;
      color: #475569;
      line-height: 1.5;
    }
    .tbl-link {
      font-size: 0.84rem;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      white-space: nowrap;
    }
    .tbl-link--web {
      color: #0F172A;
    }
    .tbl-link--web:hover {
      color: #2563EB;
      text-decoration: underline;
    }
    .tbl-link--gbp {
      color: #15803D;
    }
    .tbl-link--gbp:hover {
      color: #166534;
      text-decoration: underline;
    }
    .tbl-dim {
      color: #94A3B8;
      font-size: 1rem;
    }
    .arr {
      font-size: 0.85rem;
      transition: transform 0.15s ease;
    }
    .tbl-link:hover .arr {
      transform: translate(2px, -2px);
    }
  </style>
'''

table_script = '''
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const searchInput = document.getElementById('dirSearchInput');
      const tableBody = document.getElementById('dirTableBody');
      const rows = tableBody ? tableBody.querySelectorAll('tr.dir-row') : [];
      const noMatch = document.getElementById('noMatchMsg');

      if (searchInput && rows.length > 0) {
        searchInput.addEventListener('input', function() {
          const query = this.value.toLowerCase().trim();
          let visibleCount = 0;
          
          rows.forEach(function(row) {
            const data = row.getAttribute('data-search') || '';
            if (!query || data.includes(query)) {
              row.style.display = '';
              visibleCount++;
            } else {
              row.style.display = 'none';
            }
          });

          if (noMatch) {
            noMatch.style.display = visibleCount === 0 ? 'block' : 'none';
          }
        });
      }
    });
  </script>
'''

# 1. GENERATE STATIC HTML
full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEO Experts in Nepal | Smaran Raut</title>
  <meta name="description" content="Explore verified profiles of SEO experts in Nepal. Compare technical specialisations, local map rankings, consulting fee models, and vetting standards.">
  <link rel="canonical" href="https://smaranraut.com.np/blog/top-seo-experts-in-nepal/">
  <meta name="robots" content="index, follow">

  <!-- Critical Layout Fallback -->
  <style>
    :root {{
      --primary-dark: #1A1F1D;
      --accent-teal: #245037;
      --accent-gold: #8F6B38;
      --text-slate: #38403C;
      --bg-light: #FAF8F5;
    }}
    body {{
      margin: 0;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-light);
      color: var(--text-slate);
    }}
    .mobile-nav-drawer, .modal-backdrop {{
      display: none !important;
    }}
    .modal-backdrop.active, .mobile-nav-drawer.active {{
      display: flex !important;
    }}
  </style>

  <!-- Dual-Compatible Stylesheets -->
  <!-- Site Icon / Favicons -->
  <link rel="icon" type="image/png" sizes="32x32" href="../../images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="../../images/android-chrome-192x192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="../../images/apple-touch-icon.png">
  <link rel="stylesheet" href="../../css/styles.css?v=2026_v4">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">

{editorial_css}

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://smaranraut.com.np/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Knowledge Hub", "item": "https://smaranraut.com.np/blog/" }},
          {{ "@type": "ListItem", "position": 3, "name": "SEO Experts in Nepal", "item": "https://smaranraut.com.np/blog/top-seo-experts-in-nepal/" }}
        ]
      }},
      {{
        "@type": "Article",
        "headline": "SEO Experts in Nepal",
        "author": {{ "@type": "Person", "name": "Smaran Raut", "url": "https://smaranraut.com.np/" }},
        "publisher": {{ "@type": "Organization", "name": "Smaran Raut SEO & Web Development", "url": "https://smaranraut.com.np/" }},
        "datePublished": "2026-11-24",
        "dateModified": "2026-11-25",
        "mainEntityOfPage": "https://smaranraut.com.np/blog/top-seo-experts-in-nepal/",
        "description": "An authoritative editorial directory evaluating verified SEO experts in Nepal. Features detailed practitioner profiles, technical specialisations, agency comparisons, and vetting standards."
      }}
    ]
  }}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container nav-container">
      <a href="../../index.html" class="brand-logo" aria-label="Smaran Raut Home">
        <img src="../../images/logo.png" alt="Smaran Raut Logo" class="brand-logo-img" width="46" height="46">
        <div class="brand-text">
          <span class="brand-name">Smaran Raut</span>
          <span class="brand-subtitle">SEO &amp; Web Development</span>
        </div>
      </a>
      <nav class="desktop-nav" aria-label="Main Navigation">
        <a href="../../index.html" class="nav-link">Home</a>
        
        <!-- Services Dropdown -->
        <div class="nav-dropdown">
          <button class="dropdown-toggle" aria-expanded="false" aria-haspopup="true">
            Services <span class="dropdown-arrow">&#9662;</span>
          </button>
          <div class="dropdown-menu">
            <div class="dropdown-menu-header">
              <span class="dropdown-section-title">Core Services</span>
            </div>
            <a href="../../services/index.html" class="dropdown-item featured">
              <span class="item-title">All Services Overview &rarr;</span>
              <span class="item-desc">Browse our complete service offering</span>
            </a>
            <div class="dropdown-divider"></div>
            <a href="../../services/seo-optimized-web-development/index.html" class="dropdown-item">
              <span class="item-title">SEO-Optimized Web Development</span>
              <span class="item-desc">Clean, fast business websites built for search</span>
            </a>
            <a href="../../services/local-seo-itahari/index.html" class="dropdown-item">
              <span class="item-title">Local SEO & Google Maps</span>
              <span class="item-desc">Rank locally in Itahari, Dharan & Biratnagar</span>
            </a>
            <a href="../../services/technical-seo-audit/index.html" class="dropdown-item">
              <span class="item-title">SEO for Existing Websites</span>
              <span class="item-desc">Diagnostic audits and search ranking fixes</span>
            </a>
            <a href="../../services/core-web-vitals-speed/index.html" class="dropdown-item">
              <span class="item-title">Website Maintenance & Speed</span>
              <span class="item-desc">Mobile optimization and ongoing technical care</span>
            </a>
            <a href="../../services/ecommerce-seo-nepal/index.html" class="dropdown-item">
              <span class="item-title">E-Commerce SEO Nepal</span>
              <span class="item-desc">Product structured data and store visibility</span>
            </a>
            <a href="../../services/enterprise-link-building/index.html" class="dropdown-item">
              <span class="item-title">Ongoing Website Management</span>
              <span class="item-desc">Monthly search tracking and site management</span>
            </a>
          </div>
        </div>

        <!-- Knowledge Hub Dropdown -->
        <div class="nav-dropdown">
          <button class="dropdown-toggle" aria-expanded="false" aria-haspopup="true">
            Knowledge Hub <span class="dropdown-arrow">&#9662;</span>
          </button>
          <div class="dropdown-menu">
            <div class="dropdown-menu-header">
              <span class="dropdown-section-title">Educational Guides</span>
            </div>
            <a href="../index.html" class="dropdown-item featured">
              <span class="item-title">Knowledge Hub Directory &rarr;</span>
              <span class="item-desc">Explore practical web &amp; SEO guides</span>
            </a>
            <div class="dropdown-divider"></div>
            <a href="index.html" class="dropdown-item">
              <span class="item-title">SEO Experts in Nepal</span>
              <span class="item-desc">Editorial directory of leading specialists</span>
            </a>
            <a href="../google-business-profile-optimization-nepal/index.html" class="dropdown-item">
              <span class="item-title">Google Maps & Local SEO</span>
              <span class="item-desc">Profile optimization & citations in Nepal</span>
            </a>
            <a href="../nextjs-vs-wordpress-for-seo/index.html" class="dropdown-item">
              <span class="item-title">Web Development & Speed</span>
              <span class="item-desc">Framework comparisons & mobile performance</span>
            </a>
            <a href="../schema-markup-implementation-guide/index.html" class="dropdown-item">
              <span class="item-title">Technical Audits & Schema</span>
              <span class="item-desc">Structured data and indexation fixes</span>
            </a>
            <a href="../topical-authority-clustering-framework/index.html" class="dropdown-item">
              <span class="item-title">Content & Link Strategy</span>
              <span class="item-desc">Topical clusters and natural link acquisition</span>
            </a>
          </div>
        </div>

        <a href="../../case-studies/index.html" class="nav-link">Case Studies</a>
        <a href="../../about-us/index.html" class="nav-link">About</a>
        <a href="../../contact-us/index.html" class="nav-link">Contact</a>
      </nav>
      <div class="header-cta-group">
        <button class="btn btn-primary btn-consultation" data-modal="consultation">Book Consultation</button>
        <button class="mobile-menu-btn" id="mobile-menu-toggle" aria-label="Open Navigation Menu">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </header>
  
  <div class="mobile-nav-drawer" id="mobile-nav-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation" style="display: none;">
    <div class="mobile-drawer-header">
      <div class="brand-logo">
        <img src="../../images/logo.png" alt="Smaran Raut Logo" class="brand-logo-img" width="40" height="40">
        <div class="brand-text">
          <span class="brand-name">Smaran Raut</span>
          <span class="brand-subtitle">SEO &amp; Web Development</span>
        </div>
      </div>
      <button class="modal-close-btn" id="mobile-menu-close" aria-label="Close Navigation Menu">&times;</button>
    </div>
    <ul class="mobile-nav-links">
      <li><a href="../../index.html">Home</a></li>
      
      <!-- Mobile Services Dropdown -->
      <li class="mobile-dropdown-item">
        <button class="mobile-dropdown-toggle" aria-expanded="false">
          <span>Services</span>
          <span class="mobile-arrow">&#9662;</span>
        </button>
        <ul class="mobile-submenu" style="display: none;">
          <li><a href="../../services/index.html"><strong>Services Overview &rarr;</strong></a></li>
          <li><a href="../../services/seo-optimized-web-development/index.html">SEO Web Development</a></li>
          <li><a href="../../services/local-seo-itahari/index.html">Local SEO Itahari & Maps</a></li>
          <li><a href="../../services/technical-seo-audit/index.html">SEO for Existing Websites</a></li>
          <li><a href="../../services/core-web-vitals-speed/index.html">Maintenance & Speed</a></li>
          <li><a href="../../services/ecommerce-seo-nepal/index.html">E-Commerce SEO Nepal</a></li>
          <li><a href="../../services/enterprise-link-building/index.html">Ongoing Website Management</a></li>
        </ul>
      </li>

      <!-- Mobile Knowledge Hub Dropdown -->
      <li class="mobile-dropdown-item">
        <button class="mobile-dropdown-toggle" aria-expanded="false">
          <span>Knowledge Hub</span>
          <span class="mobile-arrow">&#9662;</span>
        </button>
        <ul class="mobile-submenu" style="display: none;">
          <li><a href="../index.html"><strong>Knowledge Hub Directory &rarr;</strong></a></li>
          <li><a href="index.html"><strong>SEO Experts in Nepal</strong></a></li>
          <li><a href="../google-business-profile-optimization-nepal/index.html">Google Maps & Local SEO</a></li>
          <li><a href="../nextjs-vs-wordpress-for-seo/index.html">Web Development & Speed</a></li>
          <li><a href="../schema-markup-implementation-guide/index.html">Technical SEO & Schema</a></li>
          <li><a href="../topical-authority-clustering-framework/index.html">Content & Link Strategy</a></li>
        </ul>
      </li>

      <li><a href="../../case-studies/index.html">Case Studies</a></li>
      <li><a href="../../about-us/index.html">About Smaran Raut</a></li>
      <li><a href="../../office-location/index.html">Office Location</a></li>
      <li><a href="../../contact-us/index.html">Contact</a></li>
    </ul>
    <div style="padding: 1.5rem 0;">
      <button class="btn btn-primary btn-consultation" data-modal="consultation" style="width: 100%;">Book Consultation</button>
    </div>
  </div>

  <main id="main-content">
    <section class="hero-section hero-directory">
      <div class="container container-narrow" style="position: relative; z-index: 2;">
        <div class="breadcrumbs" style="color: #94A3B8; margin-bottom: 1.25rem; font-size: 0.9rem;">
          <a href="../../index.html" style="color: #CBD5E1; text-decoration: none;">Home</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
          <a href="../index.html" style="color: #CBD5E1; text-decoration: none;">Knowledge Hub</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
          <span style="color: #FFFFFF;">SEO Experts in Nepal</span>
        </div>
        <div style="margin-bottom: 1rem;">
          <span class="badge" style="background: rgba(36, 80, 55, 0.85); color: #A7F3D0; border: 1px solid rgba(110, 231, 183, 0.3); padding: 0.35rem 0.85rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Editorial Industry Directory &middot; 2026 Edition</span>
        </div>
        <h1 class="hero-title" style="font-size: clamp(2rem, 4vw, 2.85rem); font-weight: 800; color: #FFFFFF; line-height: 1.2; margin: 0 0 1rem 0; letter-spacing: -0.02em;">SEO Experts in Nepal</h1>
        <p class="hero-subtitle" style="font-size: 1.15rem; color: #CBD5E1; max-width: 720px; line-height: 1.65; margin: 0;">
          A curated, research-grounded directory of 9 verified search engine optimisation specialists, technical web consultants, and agency founders driving organic growth across Nepal.
        </p>
      </div>
    </section>

    <div class="container container-narrow" style="padding: 3.5rem 1.5rem;">
      <article class="article-body">
{article_prose}
      </article>
    </div>
  </main>

{table_script}

  <!-- Universal Consultation Modal Dialog -->
  <div class="modal-backdrop" id="consultation-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" style="display: none;">
    <div class="modal-card">
      <div class="modal-header">
        <div>
          <h3 id="modal-title" style="margin-bottom: 0.25rem;">Schedule a Consultation</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0;">Direct discussion with Smaran Raut</p>
        </div>
        <button class="modal-close-btn" aria-label="Close dialog">&times;</button>
      </div>
      <div class="modal-body">
        <form id="consultation-form" name="consultation-modal" method="POST" data-netlify="true" netlify-honeypot="bot-field" novalidate>
          <input type="hidden" name="form-name" value="consultation-modal">
          <p style="display: none;" aria-hidden="true">
            <label>Don’t fill this out if you're human: <input name="bot-field" tabindex="-1"></label>
          </p>
          <div class="form-group">
            <label for="client-name">Full Name *</label>
            <input type="text" id="client-name" name="client_name" required placeholder="e.g. Ramesh Karki" class="form-control">
          </div>
          <div class="form-group">
            <label for="client-email">Email Address *</label>
            <input type="email" id="client-email" name="client_email" required placeholder="ramesh@company.com" class="form-control">
          </div>
          <div class="form-group">
            <label for="client-phone">Phone / WhatsApp Number *</label>
            <input type="tel" id="client-phone" name="client_phone" required placeholder="+977 9714539838" class="form-control">
          </div>
          <div class="form-group">
            <label for="client-website">Website URL (if you have one)</label>
            <input type="url" id="client-website" name="client_website" placeholder="https://yourwebsite.com" class="form-control">
          </div>
          <div class="form-group">
            <label for="modal-service-select">What do you need help with?</label>
            <select id="modal-service-select" name="service_interest" class="form-control">
              <option value="web-development">New SEO-Optimized Website Development</option>
              <option value="local-seo">Local SEO & Google Maps (Itahari & Eastern Nepal)</option>
              <option value="technical-audit">SEO Audit & Improvements for Existing Site</option>
              <option value="core-web-vitals">Website Maintenance & Speed Improvements</option>
              <option value="ecommerce-seo">E-Commerce Store Optimization</option>
            </select>
          </div>
          <div class="form-group">
            <label for="client-notes">Tell us about your project</label>
            <textarea id="client-notes" name="client_notes" rows="3" class="form-control" placeholder="Briefly describe your business and what you would like to achieve..."></textarea>
          </div>
          <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 0.5rem;">
            Submit Request
          </button>
          <p style="font-size: 0.75rem; color: var(--text-muted); text-align: center; margin-top: 0.85rem; margin-bottom: 0;">
            100% Confidential. In compliance with Nepal Data Protection regulations.
          </p>
        </form>
      </div>
    </div>
  </div>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand-title">Smaran Raut</div>
          <p style="color: #94A3B8; font-size: 0.92rem; margin-bottom: 1.25rem;">SEO Specialist &amp; Web Developer based in Itahari, Sunsari, Koshi Province, Nepal.</p>
          <p style="font-size: 0.85rem; color: #64748B;"><strong>Office:</strong> Main Road, Ward 4, Itahari, Sunsari 56705, Nepal<br><strong>Inquiries:</strong> contact@smaranraut.com.np &middot; +977 9714539838</p>
        </div>
        <div>
          <div class="footer-col-title">Services</div>
          <ul class="footer-links">
            <li><a href="../../services/index.html">Services Overview</a></li>
            <li><a href="../../services/seo-optimized-web-development/index.html">SEO Web Development</a></li>
            <li><a href="../../services/local-seo-itahari/index.html">Local SEO Itahari</a></li>
            <li><a href="../../services/technical-seo-audit/index.html">SEO for Existing Sites</a></li>
            <li><a href="../../services/core-web-vitals-speed/index.html">Maintenance &amp; Speed</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Knowledge Hub</div>
          <ul class="footer-links">
            <li><a href="../index.html">All Helpful Guides</a></li>
            <li><a href="index.html">SEO Experts in Nepal</a></li>
            <li><a href="../website-setup-and-management/index.html">Website Setup &amp; Management</a></li>
            <li><a href="../seo-services-explained/index.html">SEO Services Explained</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">About &amp; Legal</div>
          <ul class="footer-links">
            <li><a href="../../about-us/index.html">About Smaran Raut</a></li>
            <li><a href="../../case-studies/index.html">Client Case Studies</a></li>
            <li><a href="../../office-location/index.html">Office Location</a></li>
            <li><a href="../../consultation/index.html">Schedule a Consultation</a></li>
            <li><a href="../../disclaimer/index.html">Professional Disclaimer</a></li>
            <li><a href="../../privacy-policy/index.html">Privacy Policy</a></li>
            <li><a href="../../terms-and-conditions/index.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-statutory-notes">&copy; 2026 Smaran Raut SEO &amp; Web Development. Registered under OCR &amp; IRD PAN/VAT Act 2058, Nepal.</div>
        <div><a href="https://g.page/r/CXbkZaR8nj4kEBM/review" target="_blank" rel="noopener noreferrer" style="color: var(--accent-teal); font-size: 0.85rem; margin-right: 1rem;">Smaran Raut - No.1 SEO Expert in Itahari</a>
          <a href="../../sitemap.xml" style="color: var(--accent-teal); font-size: 0.85rem; margin-right: 1rem;">XML Sitemap</a><a href="../../robots.txt" style="color: var(--accent-teal); font-size: 0.85rem;">Robots.txt</a></div>
      </div>
    </div>
  </footer>

  <script src="../../js/app.js?v=2026_v4"></script>
</body>
</html>
'''

# 2. GENERATE WORDPRESS TEMPLATE PART
wp_hero_img = "<?php echo esc_url(get_template_directory_uri() . '/images/seo-experts-hero.jpg'); ?>"
wp_css = editorial_css.replace("../../images/seo-experts-hero.jpg", wp_hero_img)

wp_article_content = article_prose
wp_article_content = wp_article_content.replace('../../services/technical-seo-audit/index.html', "<?php echo esc_url(home_url('/services/technical-seo-audit/')); ?>")
wp_article_content = wp_article_content.replace('../../services/core-web-vitals-speed/index.html', "<?php echo esc_url(home_url('/services/core-web-vitals-speed/')); ?>")
wp_article_content = wp_article_content.replace('../../services/local-seo-itahari/index.html', "<?php echo esc_url(home_url('/services/local-seo-itahari/')); ?>")
wp_article_content = wp_article_content.replace('../../services/seo-optimized-web-development/index.html', "<?php echo esc_url(home_url('/services/seo-optimized-web-development/')); ?>")
wp_article_content = wp_article_content.replace('../how-seo-works/index.html', "<?php echo esc_url(home_url('/blog/how-seo-works/')); ?>")
wp_article_content = wp_article_content.replace('../google-business-profile-optimization-nepal/index.html', "<?php echo esc_url(home_url('/blog/google-business-profile-optimization-nepal/')); ?>")
wp_article_content = wp_article_content.replace('../../about-us/index.html', "<?php echo esc_url(home_url('/about-us/')); ?>")
wp_article_content = wp_article_content.replace('../../contact-us/index.html', "<?php echo esc_url(home_url('/contact-us/')); ?>")
wp_article_content = wp_article_content.replace('../../services/index.html', "<?php echo esc_url(home_url('/services/')); ?>")

full_wp = f'''<?php
// Blog Guide Part: SEO Experts in Nepal - Refined Editorial Directory (Forbes Style)
if (!defined('ABSPATH')) exit;
?>
{wp_css}
<main id="main-content">
  <section class="hero-section hero-directory">
    <div class="container container-narrow" style="position: relative; z-index: 2;">
      <div class="breadcrumbs" style="color: #94A3B8; margin-bottom: 1.25rem; font-size: 0.9rem;">
        <a href="<?php echo esc_url(home_url('/')); ?>" style="color: #CBD5E1; text-decoration: none;">Home</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
        <a href="<?php echo esc_url(home_url('/blog/')); ?>" style="color: #CBD5E1; text-decoration: none;">Knowledge Hub</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
        <span style="color: #FFFFFF;">SEO Experts in Nepal</span>
      </div>
      <div style="margin-bottom: 1rem;">
        <span class="badge" style="background: rgba(36, 80, 55, 0.85); color: #A7F3D0; border: 1px solid rgba(110, 231, 183, 0.3); padding: 0.35rem 0.85rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Editorial Industry Directory &middot; 2026 Edition</span>
      </div>
      <h1 class="hero-title" style="font-size: clamp(2rem, 4vw, 2.85rem); font-weight: 800; color: #FFFFFF; line-height: 1.2; margin: 0 0 1rem 0; letter-spacing: -0.02em;">SEO Experts in Nepal</h1>
      <p class="hero-subtitle" style="font-size: 1.15rem; color: #CBD5E1; max-width: 720px; line-height: 1.65; margin: 0;">
        A curated, research-grounded directory of 9 verified search engine optimisation specialists, technical web consultants, and agency founders driving organic growth across Nepal.
      </p>
    </div>
  </section>

  <div class="container container-narrow" style="padding: 3.5rem 1.5rem;">
    <article class="article-body">
{wp_article_content}
    </article>
  </div>
</main>

{table_script}
'''

# 3. WRITE THE ARTICLE FILES
with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Written refined HTML to {html_path} ({len(full_html)} bytes)")

with open(wp_path, "w", encoding="utf-8") as f:
    f.write(full_wp)
print(f"Written refined WordPress template to {wp_path} ({len(full_wp)} bytes)")

# 4. UPDATE KNOWLEDGE HUB CARD TITLE IN BLOG/INDEX.HTML AND PAGE-BLOG.PHP
with open(blog_index_path, "r", encoding="utf-8") as f:
    b_html = f.read()
b_html = b_html.replace(
    'Top SEO Experts in Nepal: Verified Professional Directory',
    'SEO Experts in Nepal: Verified Professional Directory'
)
with open(blog_index_path, "w", encoding="utf-8") as f:
    f.write(b_html)
print("Updated card title in blog/index.html")

with open(page_blog_path, "r", encoding="utf-8") as f:
    b_wp = f.read()
b_wp = b_wp.replace(
    'Top SEO Experts in Nepal: Verified Professional Directory',
    'SEO Experts in Nepal: Verified Professional Directory'
)
with open(page_blog_path, "w", encoding="utf-8") as f:
    f.write(b_wp)
print("Updated card title in page-blog.php")

# 5. UPDATE DROPDOWN TITLE IN HEADER.PHP
with open(header_wp_path, "r", encoding="utf-8") as f:
    h_wp = f.read()
h_wp = h_wp.replace(
    '<span class="item-title">Top SEO Experts in Nepal</span>',
    '<span class="item-title">SEO Experts in Nepal</span>'
)
h_wp = h_wp.replace(
    '<strong>Top SEO Experts in Nepal</strong>',
    '<strong>SEO Experts in Nepal</strong>'
)
with open(header_wp_path, "w", encoding="utf-8") as f:
    f.write(h_wp)
print("Updated nav title in header.php")
