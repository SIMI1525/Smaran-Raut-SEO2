# Refined Builder for "Top SEO Experts in Nepal"
import os

html_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\top-seo-experts-in-nepal\index.html"
wp_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\top-seo-experts-in-nepal.php"

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

# Refined Article Content with Koray-style Topical Authority and Internal Linking
article_content = f'''
      <!-- Editorial Intro Section -->
      <section class="editorial-intro-block" style="margin-bottom: 2.75rem;">
        <p class="lead-text" style="font-size: 1.15rem; line-height: 1.75; color: #1E293B; margin-bottom: 1.5rem;">
          Organic search presence has evolved into one of the most commercially significant digital channels for enterprises across Nepal. As decision-makers, consumers, and overseas diaspora audiences increasingly turn to search engines to evaluate healthcare providers, colleges, eCommerce portals, legal practices, and B2B services, ranking prominently on Google delivers qualified, conversion-ready inquiries without the compounding ad-spend fatigue of social media advertising.
        </p>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 1.5rem;">
          However, high-performance search marketing requires specialized technical discipline. Modern search engine optimization spans rigorous <a href="../../services/technical-seo-audit/index.html">technical SEO diagnostics</a>, server-side crawl budget management, mobile <a href="../../services/core-web-vitals-speed/index.html">Core Web Vitals performance</a>, high-intent localized search visibility via <a href="../../services/local-seo-itahari/index.html">Google Business Profile optimization</a>, and clean, search-ready <a href="../../services/seo-optimized-web-development/index.html">website development</a>.
        </p>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 2rem;">
          To help business owners, founders, and marketing directors navigate Nepal's expanding search marketing landscape, this curated directory presents verified professional profiles of 9 practicing SEO specialists, technical consultants, and agency leaders.
        </p>

        <!-- Editorial Directory Transparency Policy -->
        <div class="editorial-transparency-card" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid var(--accent-teal, #245037); padding: 1.25rem 1.5rem; border-radius: 6px; margin-bottom: 2rem;">
          <div style="font-weight: 700; font-size: 1rem; color: #0F172A; margin-bottom: 0.4rem; display: flex; align-items: center; gap: 0.5rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            Editorial Policy &amp; Selection Criteria
          </div>
          <p style="margin: 0; font-size: 0.92rem; line-height: 1.6; color: #475569;">
            This listing is an independent editorial compilation based on publicly verifiable practitioner websites, documented portfolio projects, technical client results, and established contributions to the local SEO community in Nepal. It does not represent a commercial competition, sponsored placement, or official accreditation board. Professionals are presented in a neutral sequential format to facilitate direct evaluation of their locations, core specialisations, and published credentials.
          </p>
        </div>
      </section>

      <!-- H2: Editorial Directory Table (Forbes Style) -->
      <section class="editorial-table-section" style="margin-bottom: 3.5rem;">
        <div class="table-header-group" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">
          <div>
            <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin: 0 0 0.35rem 0;">SEO Experts in Nepal</h2>
            <div style="font-size: 0.92rem; color: #64748B;">Curated directory of 9 verified search specialists and technical consultants</div>
          </div>
          <div class="table-filter-box" style="position: relative; min-width: 280px;">
            <input type="text" id="dirSearchInput" placeholder="Filter by name, location, skill..." style="width: 100%; padding: 0.55rem 0.85rem 0.55rem 2.25rem; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.88rem; outline: none; background: #FFFFFF; color: #1E293B;">
            <svg style="position: absolute; left: 0.75rem; top: 50%; transform: translateY(-50%); color: #94A3B8; pointer-events: none;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </div>
        </div>

        <!-- Desktop & Tablet Editorial Table -->
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
          No professionals matched your filter criteria. Try searching for "Kathmandu", "Local SEO", "Technical", or a specialist's name.
        </div>
      </section>

      <!-- H2: How to Choose Section -->
      <section class="guide-content-section" style="margin-bottom: 3.5rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">How to Choose the Right SEO Expert in Nepal</h2>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 2rem;">
          Engaging an SEO consultant directly influences your website's organic customer acquisition, brand credibility, and search engine crawl stability. When interviewing practitioners in Nepal, evaluate their qualifications across these six operational criteria:
        </p>

        <div class="evaluation-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">1</span>
              Technical SEO Knowledge
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              A qualified specialist must demonstrate deep familiarity with server response codes, XML sitemap configurations, canonicalization rules, and robots.txt directives. They should know how to diagnose crawl traps, handle JavaScript hydration bottlenecks, and optimize Core Web Vitals (LCP, INP, CLS) for mobile users in Nepal.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">2</span>
              Local SEO &amp; Google Maps Capabilities
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Local business success in Nepal relies heavily on Google Map Pack placement. Verify whether the consultant understands local citation building, Name-Address-Phone (NAP) consistency across directories, and category associations on Google Business Profile to capture foot traffic in Kathmandu, Lalitpur, Pokhara, Itahari, and Biratnagar.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">3</span>
              Verifiable Case Studies &amp; Portfolios
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Request tangible evidence of past organic search campaigns. Reputable practitioners will share anonymized Google Search Console impressions, organic click trends, or live search rankings achieved for clients in competitive industries such as education, travel, medical services, and eCommerce.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">4</span>
              Communication &amp; Transparent Reporting
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Inquire about reporting frequency and metrics. Professional consultants avoid confusing jargon and focus on transparent metrics: qualified search clicks, indexation coverage, conversion inquiries, and organic lead acquisition tracked via Google Analytics 4 (GA4) and Google Search Console.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">5</span>
              Ethical White-Hat Standards
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Confirm that the consultant complies strictly with Google Search Essentials. Deceptive shortcuts such as automated backlink generators, private blog networks (PBNs), and scraped content risk algorithmic penalties or manual actions that can permanently damage a business domain's reputation.
            </p>
          </div>

          <div class="eval-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin: 0 0 0.65rem 0; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.8rem; font-weight: 700;">6</span>
              Realistic Timelines &amp; Integrity
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Be cautious of guarantees promising "number one rankings in 7 days." Organic search requires discovery, crawl budget allocation, indexing, and algorithmic trust building. An honest consultant will outline a realistic 3- to 6-month roadmap with clear intermediate milestones.
            </p>
          </div>
        </div>
      </section>

      <!-- H2: Freelance SEO Expert vs SEO Agency -->
      <section class="guide-content-section" style="margin-bottom: 3.5rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">Freelance SEO Expert vs SEO Agency</h2>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 1.75rem;">
          When investing in organic search, Nepali enterprises typically choose between hiring an independent freelance SEO consultant or partnering with an established digital marketing agency. Both arrangements have distinct operational characteristics:
        </p>

        <div class="table-container-responsive" style="overflow-x: auto; margin-bottom: 2rem;">
          <table style="width: 100%; min-width: 680px; border-collapse: collapse; text-align: left; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; font-size: 0.92rem;">
            <thead>
              <tr style="background: #F8FAFC; border-bottom: 2px solid #E2E8F0; color: #0F172A;">
                <th style="padding: 1rem 1.25rem; font-weight: 700;">Operational Dimension</th>
                <th style="padding: 1rem 1.25rem; font-weight: 700;">Independent Consultant / Freelancer</th>
                <th style="padding: 1rem 1.25rem; font-weight: 700;">Full-Service Digital Agency</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Direct Communication</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Direct collaboration with the technical specialist implementing code, content, and schema changes.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Communication typically routed through dedicated account managers and support ticketing queues.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Technical Focus</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Intensive focus on site architecture, Core Web Vitals, indexation hygiene, and customized local maps optimization.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Broader digital marketing scope often combining SEO with social ads, graphic design, and PR outreach.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Content Production Scale</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Strategic content briefs and optimization; often collaborates with the client's internal subject matter experts.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">High content volume delivered through dedicated in-house copywriters, translators, and creative designers.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Fee Structure</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Lower operational overhead; fees correlate directly to specialist hours, technical audits, and performance milestones.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Higher monthly retainers to sustain office overhead, account management staff, and multi-team operations.</td>
              </tr>
              <tr>
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Best Suited For</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Growing businesses, local clinics, regional retailers, and startups seeking agile execution and specialized technical guidance.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">National corporations, commercial banks, and enterprises requiring multi-channel creative execution across multiple media.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- H2: Frequently Asked Questions -->
      <section class="guide-content-section" style="margin-bottom: 3.5rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">Frequently Asked Questions</h2>
        
        <div class="faq-list" style="display: flex; flex-direction: column; gap: 1.25rem;">
          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">Who are some SEO experts in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Nepal is home to a dedicated group of verified search practitioners and consultants. Key professionals documented in this directory include Smaran Raut (Web Developer &amp; SEO Expert in Itahari), Krishna Bogati (Kathmandu), Ujjwal Rupakheti (Itahari), Sushant Karn (Kathmandu), Suman Dhami (AlpineRoot), Diwakar Bhatt (Kathmandu), Suraj Giri (Bhaktapur), Dipak Paneru (Global Consultant), and Rahul Ranjan (Biratnagar).
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">What does an SEO expert do?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              An SEO expert audits, diagnoses, and enhances a website's visibility on search engines. Their daily responsibilities include fixing indexation and crawl errors, researching high-intent keywords, structuring schema markup, optimizing page speed and mobile responsiveness, building regional map pack presence on Google Business Profile, and tracking organic conversion performance through Google Search Console and GA4.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">How do I choose an SEO consultant in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Choose an SEO consultant by reviewing their verified portfolio, testing the technical health and speed of their own web domain, asking for specific case studies in your market, and verifying that they adhere strictly to Google Search Essentials. Reliable consultants provide clear explanations of crawl mechanics and set realistic timelines rather than offering instant ranking guarantees.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">How much does SEO cost in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              In Nepal, SEO pricing typically follows retainer or project-based billing. Ongoing monthly retainers for local small-to-medium businesses generally range from NPR 15,000 to NPR 45,000 per month depending on niche competitiveness and geographic scope. In-depth technical audits or custom web builds with SEO architecture start from NPR 20,000 to NPR 60,000+, while enterprise and multi-location eCommerce campaigns command higher custom project rates.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.4rem;">
            <h3 style="font-size: 1.12rem; color: #0F172A; margin: 0 0 0.5rem 0;">How long does SEO take to show results?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Most websites experience measurable improvements in crawl frequency, impressions, and query coverage within 4 to 8 weeks after addressing foundational technical issues. Meaningful keyword ranking gains and organic inquiry increases typically emerge within 3 to 6 months, compounding sustainably over 6 to 12 months as topical authority strengthens.
            </p>
          </div>
        </div>
      </section>

      <!-- Koray-Style Contextual Internal Linking Section -->
      <section class="contextual-linking-section" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 2rem; margin-bottom: 3.5rem;">
        <h3 style="font-size: 1.35rem; font-weight: 700; color: #0F172A; margin: 0 0 1rem 0;">Strategic SEO and Technical Infrastructure Guides</h3>
        <p style="font-size: 0.95rem; line-height: 1.7; color: #475569; margin-bottom: 1.25rem;">
          Evaluating search specialists is closely connected to understanding how website structure affects search engine crawling and user conversion. If you are developing a new commercial platform, exploring our <a href="../../services/seo-optimized-web-development/index.html">SEO-optimized business website development</a> services will help you establish clean semantic markup and fast static delivery right from launch.
        </p>
        <p style="font-size: 0.95rem; line-height: 1.7; color: #475569; margin-bottom: 1.25rem;">
          For businesses with existing websites suffering from dropped keyword rankings or indexation stalls, a comprehensive <a href="../../services/technical-seo-audit/index.html">technical SEO audit and site improvement</a> review can pinpoint server-side errors, redirect loops, and schema gaps. Furthermore, regional retailers looking to dominate local search queries in Sunsari, Morang, and Jhapa can discover actionable methods in our guide to <a href="../../services/local-seo-itahari/index.html">local SEO and Google Maps optimization in Itahari</a>.
        </p>
        <p style="font-size: 0.95rem; line-height: 1.7; color: #475569; margin: 0;">
          To deepen your understanding of search mechanics, read our foundational guide on <a href="../how-seo-works/index.html">how SEO works and search rankings in Nepal</a>, or explore our step-by-step framework for <a href="../google-business-profile-optimization-nepal/index.html">Google Business Profile optimization in Nepal</a>. You can also learn more <a href="../../about-us/index.html">about Smaran Raut</a> or <a href="../../contact-us/index.html">contact our team</a> directly to discuss your website's search performance.
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

# CSS for Forbes-Style Table & Hero Styling
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

# Live Filter Script
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

# 1. BUILD COMPLETE STATIC HTML FILE
full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Top SEO Experts in Nepal (2026 Directory) | Smaran Raut</title>
  <meta name="description" content="Discover and compare the top SEO experts, consultants, and specialists in Nepal. Explore verified profiles, key specialisations, service models, and hiring advice.">
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
          {{ "@type": "ListItem", "position": 3, "name": "Top SEO Experts in Nepal", "item": "https://smaranraut.com.np/blog/top-seo-experts-in-nepal/" }}
        ]
      }},
      {{
        "@type": "Article",
        "headline": "Top SEO Experts in Nepal",
        "author": {{ "@type": "Person", "name": "Smaran Raut", "url": "https://smaranraut.com.np/" }},
        "publisher": {{ "@type": "Organization", "name": "Smaran Raut SEO & Web Development", "url": "https://smaranraut.com.np/" }},
        "datePublished": "2026-11-24",
        "dateModified": "2026-11-25",
        "mainEntityOfPage": "https://smaranraut.com.np/blog/top-seo-experts-in-nepal/",
        "description": "An authoritative editorial directory and research guide reviewing the top SEO experts, consultants, and specialists in Nepal. Features verified practitioner profiles, core specialisations, agency affiliations, and hiring advice."
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
              <span class="item-title">Top SEO Experts in Nepal</span>
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
          <li><a href="index.html"><strong>Top SEO Experts in Nepal</strong></a></li>
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
          <span style="color: #FFFFFF;">Top SEO Experts in Nepal</span>
        </div>
        <div style="margin-bottom: 1rem;">
          <span class="badge" style="background: rgba(36, 80, 55, 0.85); color: #A7F3D0; border: 1px solid rgba(110, 231, 183, 0.3); padding: 0.35rem 0.85rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Editorial Industry Directory &middot; 2026 Edition</span>
        </div>
        <h1 class="hero-title" style="font-size: clamp(2rem, 4vw, 2.85rem); font-weight: 800; color: #FFFFFF; line-height: 1.2; margin: 0 0 1rem 0; letter-spacing: -0.02em;">Top SEO Experts in Nepal</h1>
        <p class="hero-subtitle" style="font-size: 1.15rem; color: #CBD5E1; max-width: 720px; line-height: 1.65; margin: 0;">
          A curated, research-grounded directory of 9 proven search engine optimisation specialists, technical web consultants, and agency founders driving organic growth across Nepal.
        </p>
      </div>
    </section>

    <div class="container container-narrow" style="padding: 3.5rem 1.5rem;">
      <article class="article-body">
{article_content}
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
            <li><a href="index.html">Top SEO Experts in Nepal</a></li>
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

# 2. BUILD WORDPRESS TEMPLATE PART
# Note: In WordPress, image path is dynamic or absolute URL
wp_hero_img = "<?php echo esc_url(get_template_directory_uri() . '/images/seo-experts-hero.jpg'); ?>"
wp_css = editorial_css.replace("../../images/seo-experts-hero.jpg", wp_hero_img)

# Replace relative links with WordPress dynamic URLs in article_content
wp_article_content = article_content
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
// Blog Guide Part: Top SEO Experts in Nepal - Refined Editorial Directory (Forbes Style)
if (!defined('ABSPATH')) exit;
?>
{wp_css}
<main id="main-content">
  <section class="hero-section hero-directory">
    <div class="container container-narrow" style="position: relative; z-index: 2;">
      <div class="breadcrumbs" style="color: #94A3B8; margin-bottom: 1.25rem; font-size: 0.9rem;">
        <a href="<?php echo esc_url(home_url('/')); ?>" style="color: #CBD5E1; text-decoration: none;">Home</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
        <a href="<?php echo esc_url(home_url('/blog/')); ?>" style="color: #CBD5E1; text-decoration: none;">Knowledge Hub</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
        <span style="color: #FFFFFF;">Top SEO Experts in Nepal</span>
      </div>
      <div style="margin-bottom: 1rem;">
        <span class="badge" style="background: rgba(36, 80, 55, 0.85); color: #A7F3D0; border: 1px solid rgba(110, 231, 183, 0.3); padding: 0.35rem 0.85rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Editorial Industry Directory &middot; 2026 Edition</span>
      </div>
      <h1 class="hero-title" style="font-size: clamp(2rem, 4vw, 2.85rem); font-weight: 800; color: #FFFFFF; line-height: 1.2; margin: 0 0 1rem 0; letter-spacing: -0.02em;">Top SEO Experts in Nepal</h1>
      <p class="hero-subtitle" style="font-size: 1.15rem; color: #CBD5E1; max-width: 720px; line-height: 1.65; margin: 0;">
        A curated, research-grounded directory of 9 proven search engine optimisation specialists, technical web consultants, and agency founders driving organic growth across Nepal.
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

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Refined HTML written to {html_path} ({len(full_html)} bytes)")

with open(wp_path, "w", encoding="utf-8") as f:
    f.write(full_wp)
print(f"Refined WP template written to {wp_path} ({len(full_wp)} bytes)")
