import os

html_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\top-seo-experts-in-nepal\index.html"
wp_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\top-seo-experts-in-nepal.php"

os.makedirs(os.path.dirname(html_path), exist_ok=True)
os.makedirs(os.path.dirname(wp_path), exist_ok=True)

profiles = [
    {
        "initials": "SR",
        "name": "Smaran Raut",
        "title": "Web Developer & SEO Expert",
        "location": "Itahari, Nepal",
        "company": None,
        "desc": "Smaran Raut is a web developer and SEO expert based in Itahari, Nepal. He focuses on developing professional, SEO-optimised websites and helping businesses improve their online visibility through search engine optimisation, local SEO, Google Business Profile optimisation, keyword research, content optimisation, and website management.",
        "specs": [
            "Search Engine Optimisation",
            "Local SEO",
            "Website Design & Development",
            "Technical SEO",
            "Keyword Research",
            "Content Optimisation",
            "Google Business Profile Optimisation"
        ],
        "website": "https://smaranraut.com.np/",
        "linkedin": "https://www.linkedin.com/in/smaran-raut",
        "gbp": "https://g.page/r/CXbkZaR8nj4kEBM/review"
    },
    {
        "initials": "KB",
        "name": "Krishna Bogati",
        "title": "SEO Expert & WordPress Specialist",
        "location": "Kathmandu, Nepal",
        "company": None,
        "desc": "Krishna Bogati is an SEO specialist and WordPress developer based in Kathmandu, Nepal. He focuses on comprehensive website audits, organic search ranking strategies, WordPress performance tuning, and optimizing digital assets for modern AI and search engines.",
        "specs": [
            "Technical SEO & Crawl Audits",
            "WordPress Development & Optimisation",
            "On-Page SEO & Content Strategy",
            "AI Search Engine Optimisation"
        ],
        "website": "https://krishnabogati.com.np/",
        "linkedin": "https://www.linkedin.com/in/krishbogati/",
        "gbp": None
    },
    {
        "initials": "UR",
        "name": "Ujjwal Rupakheti",
        "title": "Web Developer & SEO Specialist",
        "location": "Itahari, Nepal",
        "company": None,
        "desc": "Ujjwal Rupakheti is a web developer and SEO specialist operating from Itahari, Nepal. He builds clean, search-ready websites and web applications tailored for local businesses and growing brands, emphasizing fast page delivery, technical structure, and regional search visibility.",
        "specs": [
            "Website Development & Design",
            "Technical SEO Infrastructure",
            "Local Business SEO",
            "Core Web Vitals & Site Speed"
        ],
        "website": "https://www.ujjwalrupakheti.com.np/",
        "linkedin": "https://www.linkedin.com/in/ujjwal-rupakheti-bb421b339/",
        "gbp": None
    },
    {
        "initials": "SK",
        "name": "Sushant Karn",
        "title": "SEO Consultant & Growth Specialist",
        "location": "Kathmandu, Nepal",
        "company": None,
        "desc": "Sushant Karn is an SEO consultant based in Kathmandu, Nepal. He partners with businesses to improve search rankings through structured technical diagnostics, organic search acquisition frameworks, authoritative link building, and targeted content planning.",
        "specs": [
            "SEO Consulting & Strategic Audits",
            "Technical SEO Diagnostics",
            "Link Building & Digital Outreach",
            "Search-Driven Content Strategy"
        ],
        "website": "https://sushantkarn.info.np/",
        "linkedin": "https://www.linkedin.com/in/sushantkarn",
        "gbp": None
    },
    {
        "initials": "SD",
        "name": "Suman Dhami",
        "title": "SEO Expert & Web Developer",
        "location": "Kathmandu, Nepal",
        "company": "AlpineRoot",
        "desc": "Suman Dhami is an SEO specialist and web developer working from Kathmandu, Nepal. Through his work with client businesses across Nepal and Australia as part of the AlpineRoot team, he delivers end-to-end SEO audits, ongoing search campaigns, and modern web builds.",
        "specs": [
            "Technical SEO Audits",
            "Ongoing Organic SEO Campaigns",
            "Cross-Border SEO (Nepal & Australia)",
            "Custom Website Development"
        ],
        "website": "https://sumandhami.com.np/",
        "linkedin": "https://www.linkedin.com/in/suman-dhami/",
        "gbp": None
    },
    {
        "initials": "DB",
        "name": "Diwakar Bhatt",
        "title": "SEO Specialist & Web Developer",
        "location": "Kathmandu, Nepal",
        "company": None,
        "desc": "Diwakar Bhatt is an SEO specialist and website developer based in Kathmandu, Nepal. His practice emphasizes technical search architecture, crawl efficiency, schema markup deployment, and preparing web platforms for answer engine optimization and AI-driven search models.",
        "specs": [
            "Technical SEO & Crawl Architecture",
            "Structured Data & Schema Implementation",
            "Answer Engine Optimisation (AEO)",
            "Keyword Research & On-Page Architecture"
        ],
        "website": "https://diwakarbhatt.com.np/",
        "linkedin": "https://www.linkedin.com/in/diwakar-bhatt/",
        "gbp": None
    },
    {
        "initials": "RR",
        "name": "Rahul Ranjan",
        "title": "SEO Expert & Full Stack Developer",
        "location": "Biratnagar, Nepal",
        "company": None,
        "desc": "Rahul Ranjan is an SEO specialist and full stack developer based in Biratnagar, Nepal. He integrates modern web frameworks like Next.js with in-depth technical SEO, Google Analytics 4 tracking architecture, and digital growth systems for technology and cybersecurity enterprises.",
        "specs": [
            "Technical SEO for Modern Frameworks (Next.js)",
            "Full Stack Web Engineering",
            "Google Analytics 4 & Measurement",
            "Digital Lead Generation"
        ],
        "website": "https://www.rahulranjan.com.np/",
        "linkedin": "https://www.linkedin.com/in/rahul-ranjan-dev/",
        "gbp": None
    },
    {
        "initials": "DP",
        "name": "Dipak Paneru",
        "title": "Digital Marketing & Technical SEO Specialist",
        "location": "Nepal (Global Consultant)",
        "company": None,
        "desc": "Dipak Paneru is an experienced digital marketing and SEO consultant operating from Nepal. He consults for international organizations and local companies on technical entity-based SEO, Google Map Pack rankings, and multi-region organic visibility.",
        "specs": [
            "Local SEO & Google Map Pack Strategy",
            "Technical Entity-Based SEO",
            "Multi-Region Search Strategy",
            "Digital Marketing Consulting"
        ],
        "website": "https://dipakpaneru.com/",
        "linkedin": "https://linkedin.com/in/dipakpaneru",
        "gbp": "https://g.page/r/CYU3MsvIRvvTEBM/review"
    },
    {
        "initials": "PG",
        "name": "Prabesh Ghimire",
        "title": "SEO Specialist & Growth Strategist",
        "location": "Nepal",
        "company": None,
        "desc": "Prabesh Ghimire is an SEO specialist and digital growth strategist in Nepal. He helps businesses increase qualified search traffic by developing data-led organic strategies, technical infrastructure optimizations, and local search presence.",
        "specs": [
            "Organic Search Strategy",
            "Technical SEO Auditing",
            "Local Search Optimisation",
            "Data-Driven Growth Planning"
        ],
        "website": "https://ghimireprabesh.com.np/",
        "linkedin": "https://www.linkedin.com/in/digitalprabesh/",
        "gbp": None
    },
    {
        "initials": "KJ",
        "name": "Keshab Joshi",
        "title": "SEO Specialist & Digital Consultant",
        "location": "Nepal",
        "company": None,
        "desc": "Keshab Joshi is an SEO consultant and digital advertising specialist based in Nepal. He develops and executes multi-channel visibility programs spanning technical SEO, on-page optimization, Google Ads, and Meta advertising for clients in Nepal, North America, the UK, and Australia.",
        "specs": [
            "Core & Technical SEO",
            "Local SEO & Citation Strategy",
            "Paid Search (Google Ads) Integration",
            "International Client Campaigns"
        ],
        "website": "https://krjoshi.com.np/",
        "linkedin": "https://www.linkedin.com/in/keshab-joshi",
        "gbp": None
    },
    {
        "initials": "SG",
        "name": "Suraj Giri",
        "title": "Independent SEO Consultant",
        "location": "Bhaktapur, Nepal",
        "company": None,
        "desc": "Suraj Giri is an independent SEO consultant based in Bhaktapur, Nepal. He offers transparent, hands-on search optimization services focusing on technical diagnostics, local map visibility, content optimization, and practical SEO training for business owners.",
        "specs": [
            "Independent SEO Consulting",
            "Technical Website Diagnostics",
            "Local SEO & Google Maps Placement",
            "Practical SEO Training & Audits"
        ],
        "website": "https://seoexpertinnepal.com/",
        "linkedin": "https://www.linkedin.com/in/girisuraj/",
        "gbp": "https://maps.google.com/?cid=12380517030472402827"
    },
    {
        "initials": "RT",
        "name": "Rambabu Thapa",
        "title": "Senior SEO Consultant & Agency Founder",
        "location": "Lalitpur, Nepal",
        "company": "Orka Socials",
        "desc": "Rambabu Thapa is a veteran SEO consultant and digital entrepreneur based in Lalitpur, Nepal. As the founder of Orka Socials, he has guided companies through complex technical SEO, conversion rate optimization (CRO), and enterprise search programs, while actively speaking at tech forums such as WordCamp Nepal.",
        "specs": [
            "Enterprise Technical SEO",
            "Conversion Rate Optimisation (CRO)",
            "E-Commerce Search Strategy",
            "SEO Training & Industry Mentorship"
        ],
        "website": "https://orkasocials.com/",
        "linkedin": None,
        "gbp": None
    },
    {
        "initials": "KB",
        "name": "K.K. Bhatta",
        "title": "SEO Director & Agency Founder",
        "location": "Kathmandu, Nepal",
        "company": "Queens Digital Agency",
        "desc": "K.K. Bhatta is an SEO director and the founder of Queens Digital Agency in Kathmandu, Nepal. Working in the industry since 2012, he directs corporate search engine campaigns, paid media strategies, and Answer Engine Optimization (AEO/GEO) for educational institutions, corporate entities, and automotive brands.",
        "specs": [
            "Corporate Search Engine Strategy",
            "Answer Engine Optimisation (AEO/GEO)",
            "Integrated Paid Search & PPC",
            "Technical SEO & Local Search"
        ],
        "website": "https://www.queensdigitalagency.com/seo-expert-nepal/",
        "linkedin": None,
        "gbp": None
    },
    {
        "initials": "PB",
        "name": "Pujan Bishwakarma",
        "title": "SEO Consultant & Global Search Specialist",
        "location": "Kathmandu, Nepal",
        "company": None,
        "desc": "Pujan Bishwakarma is an SEO specialist and consultant based in Kathmandu, Nepal. He works with regional and global clients on technical website health, Google Maps positioning, keyword targeting, and sustainable organic traffic growth.",
        "specs": [
            "Local SEO & Google Maps Placement",
            "Technical SEO Audits",
            "Keyword Research & On-Page SEO",
            "Global Organic Acquisition"
        ],
        "website": "https://www.pujanglobalseo.com/",
        "linkedin": None,
        "gbp": None
    },
    {
        "initials": "BT",
        "name": "Bikesh Tamang",
        "title": "SEO Specialist & Web Developer",
        "location": "Kathmandu, Nepal",
        "company": None,
        "desc": "Bikesh Tamang is an SEO specialist and web developer working in Kathmandu, Nepal. He delivers structured organic campaigns covering technical optimization, local search signals, Answer Engine Optimization (AEO), and actionable content development.",
        "specs": [
            "Technical & On-Page SEO",
            "Local Search Visibility",
            "Answer Engine Optimisation (AEO/GEO)",
            "SEO Audits & Content Planning"
        ],
        "website": "https://bikeshtamang.com.np/",
        "linkedin": "https://www.linkedin.com/in/bikeshtamang/",
        "gbp": None
    },
    {
        "initials": "AM",
        "name": "Aman Mishra",
        "title": "SEO Consultant & Digital Specialist",
        "location": "Lalitpur, Nepal",
        "company": None,
        "desc": "Aman Mishra is an SEO consultant based in Lalitpur, Nepal. He works with businesses across Nepal to audit digital properties, resolve indexing and crawling bottlenecks, optimize on-page content, and build sustainable local search rankings.",
        "specs": [
            "Technical SEO & Diagnostic Auditing",
            "On-Page & Off-Page SEO",
            "Local Business Search Optimisation",
            "Organic Lead & Traffic Growth"
        ],
        "website": "https://amanmishra.com.np/",
        "linkedin": "https://www.linkedin.com/in/aman-mishra-seo-expert/",
        "gbp": None
    }
]

def generate_cards_html():
    cards = []
    for p in profiles:
        company_markup = f'<span class="profile-company">&middot; {p["company"]}</span>' if p["company"] else ''
        specs_html = ''.join([f'<span class="profile-tag">{s}</span>' for s in p["specs"]])
        
        links = []
        if p["website"]:
            links.append(f'<a href="{p["website"]}" target="_blank" rel="noopener noreferrer" class="profile-link profile-link--web"><svg class="link-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>Official Website</a>')
        if p.get("linkedin"):
            links.append(f'<a href="{p["linkedin"]}" target="_blank" rel="noopener noreferrer" class="profile-link profile-link--linkedin"><svg class="link-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>LinkedIn</a>')
        if p.get("gbp"):
            links.append(f'<a href="{p["gbp"]}" target="_blank" rel="noopener noreferrer" class="profile-link profile-link--gbp"><svg class="link-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>Verified Google Listing</a>')
            
        links_html = '<div class="profile-links">' + ''.join(links) + '</div>'
        
        card_id = p["name"].lower().replace(' ', '-').replace('.', '')
        card = f'''          <div class="directory-card" id="{card_id}">
            <div class="profile-header">
              <div class="profile-avatar" aria-hidden="true">{p["initials"]}</div>
              <div class="profile-meta">
                <h3 class="profile-name">{p["name"]}</h3>
                <div class="profile-title">{p["title"]}</div>
                <div class="profile-location">
                  <svg class="loc-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                  <span>{p["location"]}</span>
                  {company_markup}
                </div>
              </div>
            </div>
            <p class="profile-desc">{p["desc"]}</p>
            <div class="profile-specs-wrapper">
              <span class="specs-heading">Core Focus Areas:</span>
              <div class="profile-tags">
                {specs_html}
              </div>
            </div>
            {links_html}
          </div>'''
        cards.append(card)
    return '\n'.join(cards)

cards_code = generate_cards_html()

article_body = f'''
      <!-- Editorial Intro Section -->
      <section class="guide-intro-block" style="margin-bottom: 3rem;">
        <p class="lead-text" style="font-size: 1.15rem; line-height: 1.75; color: #334155; margin-bottom: 1.5rem;">
          In an increasingly competitive digital marketplace, establishing high organic visibility across major search engines is one of the highest-leverage investments a Nepali business can make. As consumer search habits in Kathmandu, Pokhara, Lalitpur, Itahari, Biratnagar, and overseas diaspora markets mature, potential customers actively turn to Google to research local medical clinics, IT companies, colleges, hotels, eCommerce stores, and professional service providers before making a purchasing decision.
        </p>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 1.5rem;">
          Search Engine Optimisation (SEO) goes far beyond simple keyword additions. High-performance SEO involves in-depth <a href="../../services/technical-seo-audit/index.html">technical SEO diagnostics</a>, comprehensive crawlability and indexation maintenance, fast <a href="../../services/core-web-vitals-speed/index.html">Core Web Vitals delivery</a>, localized map presence through <a href="../../services/local-seo-itahari/index.html">Google Business Profile optimization</a>, and intent-focused <a href="../../services/seo-optimized-web-development/index.html">website development</a>.
        </p>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 2rem;">
          Finding the right professional can be difficult given the crowded market. This researched directory has been created to provide founders, executives, and marketers with a transparent, factual overview of practicing SEO professionals, consultants, and specialists operating in Nepal.
        </p>

        <!-- Editorial Transparency Notice -->
        <div class="editorial-notice" style="background: #F8FAFC; border-left: 4px solid var(--accent-teal, #245037); padding: 1.25rem 1.5rem; border-radius: 6px; margin-bottom: 2.5rem;">
          <h4 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; color: #0F172A; display: flex; align-items: center; gap: 0.5rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            Editorial Directory Policy &amp; Transparency
          </h4>
          <p style="margin: 0; font-size: 0.92rem; line-height: 1.6; color: #475569;">
            This compilation serves as an objective, editorial reference directory based on publicly verifiable professional information, documented company registrations, technical portfolio assets, and practitioner credentials. It does not constitute a competitive contest, commercial ranking, or paid endorsement. Professionals are presented in a neutral, continuous format to help prospective clients compare specialisations, locations, and service capabilities directly.
          </p>
        </div>
      </section>

      <!-- H2: Directory Profiles -->
      <section class="directory-section" style="margin-bottom: 4rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">SEO Experts in Nepal</h2>
        <p style="font-size: 1rem; color: #64748B; margin-bottom: 2rem;">
          Browse verified profiles of practicing search engine optimisation specialists, technical consultants, and digital agency leaders in Nepal.
        </p>

        <div class="directory-grid">
{cards_code}
        </div>
      </section>

      <!-- H2: How to Choose Section -->
      <section class="guide-content-section" style="margin-bottom: 4rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">How to Choose the Right SEO Expert in Nepal</h2>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 2rem;">
          Selecting an SEO consultant is a strategic decision that directly impacts your brand's digital revenue pipeline, search index health, and reputation. When evaluating SEO professionals in Nepal, consider these five core criteria:
        </p>

        <div class="criteria-card-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
          <div class="criteria-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.85rem; font-weight: 700;">1</span>
              Technical Competence &amp; Architecture
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Ensure your consultant understands how Google crawls and renders modern code. They should be able to audit server logs, configure XML sitemaps and robots.txt rules, implement schema structured data, resolve canonical tag pagination errors, and optimize Core Web Vitals (LCP, INP, CLS) for mobile devices.
            </p>
          </div>

          <div class="criteria-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.85rem; font-weight: 700;">2</span>
              Local Market &amp; Map Pack Nuances
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Ranking a business in Nepal requires local context. A specialist must know how Google Maps interprets local proximity in cities like Kathmandu, Lalitpur, Pokhara, Itahari, and Biratnagar, while maintaining precise Name, Address, and Phone (NAP) citations and Google Business Profile category associations.
            </p>
          </div>

          <div class="criteria-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.85rem; font-weight: 700;">3</span>
              Ethical White-Hat Standards
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Avoid any practitioner who relies on automated link networks, private blog networks (PBNs), or deceptive hidden text. Such shortcuts violate Google Search Essentials and risk algorithmic demotion or manual spam penalties that can take months to rectify.
            </p>
          </div>

          <div class="criteria-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.85rem; font-weight: 700;">4</span>
              Realistic Timelines &amp; Integrity
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Be cautious of guarantees such as "instant #1 rankings in 10 days." Organic SEO requires crawl discovery, indexation processing, algorithmic trust accumulation, and ongoing testing. Professional consultants will outline a realistic 3- to 6-month roadmap with clear intermediate milestones.
            </p>
          </div>

          <div class="criteria-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #EFF6FF; color: #2563EB; font-size: 0.85rem; font-weight: 700;">5</span>
              Transparent Reporting on Real KPIs
            </h3>
            <p style="font-size: 0.92rem; line-height: 1.6; color: #475569; margin: 0;">
              Look for specialists who report through Google Search Console and Google Analytics 4 rather than proprietary black-box dashboards. The focus of regular reporting should be on qualified organic traffic, query impressions, click-through rates, and commercial lead inquiries.
            </p>
          </div>
        </div>
      </section>

      <!-- H2: Expert vs Agency Section -->
      <section class="guide-content-section" style="margin-bottom: 4rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">SEO Expert vs SEO Agency: Which Should You Choose?</h2>
        <p style="font-size: 1.02rem; line-height: 1.7; color: #475569; margin-bottom: 1.75rem;">
          Nepali business leaders often debate whether to engage an independent consultant/freelancer or hire a full-service digital agency. Both models have clear operational strengths, and the right choice depends on your organization's internal resources, project scale, and budget.
        </p>

        <div class="table-responsive" style="overflow-x: auto; margin-bottom: 2rem;">
          <table style="width: 100%; border-collapse: collapse; text-align: left; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; font-size: 0.92rem;">
            <thead>
              <tr style="background: #F8FAFC; border-bottom: 2px solid #E2E8F0;">
                <th style="padding: 1rem 1.25rem; color: #0F172A; font-weight: 700;">Evaluation Factor</th>
                <th style="padding: 1rem 1.25rem; color: #0F172A; font-weight: 700;">Independent SEO Expert / Consultant</th>
                <th style="padding: 1rem 1.25rem; color: #0F172A; font-weight: 700;">Full-Service SEO Agency</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Communication</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Direct contact with the strategist executing the work; agile adjustments.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Managed through account managers; formal meetings and structured ticketing.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Technical Depth</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Deep hands-on execution; personal ownership of code audits and search diagnostics.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Divided among junior specialists, senior directors, and internal developers.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Content &amp; Creative Scale</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Focused strategy and briefs; often collaborates with the client's internal team.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">High production capacity with dedicated in-house writers, graphic designers, and video editors.</td>
              </tr>
              <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Cost Efficiency</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Lower operational overhead; high proportion of budget goes directly to specialist hours.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Higher retainers to support agency staffing, office overhead, and account management.</td>
              </tr>
              <tr>
                <td style="padding: 1rem 1.25rem; font-weight: 600; color: #1E293B;">Best Suited For</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Small to mid-sized businesses, startups, local service providers, and niche brands.</td>
                <td style="padding: 1rem 1.25rem; color: #475569;">Large corporations, national retail chains, and companies needing multi-channel media production.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- H2: Frequently Asked Questions -->
      <section class="guide-content-section" style="margin-bottom: 4rem;">
        <h2 class="section-title" style="font-size: 1.85rem; font-weight: 700; color: #0F172A; margin-bottom: 1.25rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 0.75rem;">Frequently Asked Questions</h2>
        
        <div class="faq-list" style="display: flex; flex-direction: column; gap: 1.5rem;">
          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.5rem;">Who are some SEO experts in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Nepal has a growing community of experienced SEO consultants, technical specialists, and agency founders. Active professionals include Smaran Raut (Web Developer &amp; SEO Expert in Itahari), Krishna Bogati (Kathmandu), Ujjwal Rupakheti (Itahari), Sushant Karn (Kathmandu), Suman Dhami (AlpineRoot), Diwakar Bhatt (Kathmandu), Rahul Ranjan (Biratnagar), Dipak Paneru (Global Consultant), Prabesh Ghimire, Keshab Joshi, Suraj Giri (Bhaktapur), Rambabu Thapa (Orka Socials), K.K. Bhatta (Queens Digital Agency), Pujan Bishwakarma, Bikesh Tamang, and Aman Mishra.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.5rem;">How do I find a reliable SEO consultant in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              To find a reliable SEO consultant, review their published case studies, check their personal website's technical performance and rankings, request specific examples of past client search growth, and conduct a discovery interview. A dependable consultant will ask detailed questions about your business goals and technical infrastructure rather than making quick, generic ranking guarantees.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.5rem;">What services does an SEO expert provide?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              An SEO expert typically delivers technical audits (resolving crawling, indexing, and mobile speed bottlenecks), keyword and commercial search intent research, on-page optimization (headings, semantic meta tags, and internal link architecture), local SEO and Google Business Profile management, high-authority backlink acquisition, and ongoing analytics tracking through Google Search Console and GA4.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.5rem;">How much does SEO cost in Nepal?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              In Nepal, SEO pricing generally operates on three common models: monthly retainers, one-off audits, or custom project fees. Monthly retainers for local small-to-medium businesses typically range from NPR 15,000 to NPR 45,000 per month depending on competitive difficulty and geographic scope. Comprehensive technical audits or custom web builds with SEO architecture generally start from NPR 20,000 to NPR 60,000+, while high-volume corporate or eCommerce campaigns command higher project budgets.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.5rem;">Should I hire a freelance SEO expert or an SEO agency?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Choose an independent SEO expert or consultant if you value direct collaboration with the specialist doing the work, require personalized technical problem-solving, or have a targeted local budget. Choose an agency if you require a comprehensive marketing team that simultaneously manages high-volume graphic design, video content production, paid media advertising, and PR alongside SEO.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.5rem;">How long does SEO take to produce results?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              For new websites, search engines typically require 3 to 6 months to crawl, evaluate, and assign reliable organic rankings. Established websites that address existing technical indexation errors or publish authoritative topical content can often see initial organic impressions and query movement within 4 to 8 weeks, with substantial business impact and lead generation compounding over 6 to 12 months.
            </p>
          </div>

          <div class="faq-item" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: #0F172A; margin-top: 0; margin-bottom: 0.5rem;">What should I check before hiring an SEO consultant?</h3>
            <p style="font-size: 0.95rem; line-height: 1.65; color: #475569; margin: 0;">
              Before signing an agreement, verify the consultant's past work and client references, inquire about the exact SEO tools they utilize (e.g. Google Search Console, Screaming Frog, Ahrefs, Semrush), clarify how often and in what format they provide progress reports, ensure you retain 100% administrative ownership of all analytics and search console properties, and confirm they strictly follow Google Search Essentials.
            </p>
          </div>
        </div>
      </section>

      <!-- CTA Box -->
      <section class="guide-cta-section" style="background: linear-gradient(135deg, #0A1628 0%, #142240 100%); color: #FFFFFF; padding: 3rem 2rem; border-radius: 12px; text-align: center; margin-bottom: 3rem;">
        <h3 style="color: #FFFFFF; font-size: 1.65rem; font-weight: 700; margin-top: 0; margin-bottom: 1rem;">Looking to Accelerate Your Organic Search Visibility?</h3>
        <p style="color: #CBD5E1; font-size: 1.05rem; max-width: 650px; margin: 0 auto 2rem; line-height: 1.6;">
          Whether you need a fresh, SEO-optimized website built from the ground up or a technical audit of your existing site, get in touch for a direct discussion about your business goals.
        </p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="../../contact-us/index.html" class="btn btn-primary" style="background: #00C2CB; color: #0A1628; font-weight: 600; padding: 0.75rem 1.75rem; border-radius: 6px; text-decoration: none; border: none;">Contact Smaran Raut &rarr;</a>
          <a href="../../services/index.html" class="btn btn-outline" style="border: 1px solid #CBD5E1; color: #FFFFFF; font-weight: 600; padding: 0.75rem 1.75rem; border-radius: 6px; text-decoration: none;">Explore Core Services</a>
        </div>
      </section>
'''

# Dedicated CSS for Directory Cards
directory_css = '''
  <style>
    /* Professional Directory Grid & Card Styles */
    .directory-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.75rem;
      margin-top: 1.5rem;
    }
    @media (max-width: 768px) {
      .directory-grid {
        grid-template-columns: 1fr;
        gap: 1.25rem;
      }
    }
    .directory-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .directory-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
      border-color: #CBD5E1;
    }
    .profile-header {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1.15rem;
    }
    .profile-avatar {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      color: #1E293B;
      font-weight: 700;
      font-size: 1.05rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      letter-spacing: 0.02em;
    }
    .profile-meta {
      flex: 1;
      min-width: 0;
    }
    .profile-name {
      font-size: 1.22rem;
      font-weight: 700;
      color: #0F172A;
      margin: 0 0 0.25rem 0;
      line-height: 1.3;
    }
    .profile-title {
      font-size: 0.88rem;
      font-weight: 600;
      color: #2563EB;
      margin-bottom: 0.35rem;
    }
    .profile-location {
      font-size: 0.82rem;
      color: #64748B;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      flex-wrap: wrap;
    }
    .profile-location .loc-icon {
      color: #94A3B8;
      flex-shrink: 0;
    }
    .profile-company {
      color: #475569;
      font-weight: 500;
    }
    .profile-desc {
      font-size: 0.92rem;
      line-height: 1.6;
      color: #334155;
      margin: 0 0 1.25rem 0;
      flex-grow: 1;
    }
    .profile-specs-wrapper {
      margin-bottom: 1.25rem;
    }
    .specs-heading {
      display: block;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #64748B;
      margin-bottom: 0.5rem;
    }
    .profile-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }
    .profile-tag {
      font-size: 0.78rem;
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      color: #334155;
      padding: 0.25rem 0.55rem;
      border-radius: 6px;
      font-weight: 500;
    }
    .profile-links {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      padding-top: 1rem;
      border-top: 1px solid #F1F5F9;
      margin-top: auto;
    }
    .profile-link {
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.65rem;
      border-radius: 6px;
      transition: background 0.15s ease, border-color 0.15s ease;
    }
    .profile-link .link-icon {
      flex-shrink: 0;
    }
    .profile-link--web {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      color: #0F172A;
    }
    .profile-link--web:hover {
      background: #F1F5F9;
      border-color: #94A3B8;
    }
    .profile-link--linkedin {
      background: #EFF6FF;
      border: 1px solid #BFDBFE;
      color: #1D4ED8;
    }
    .profile-link--linkedin:hover {
      background: #DBEAFE;
      border-color: #93C5FD;
    }
    .profile-link--gbp {
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      color: #15803D;
    }
    .profile-link--gbp:hover {
      background: #DCFCE7;
      border-color: #86EFAC;
    }
  </style>
'''

# 1. GENERATE STATIC HTML FILE
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

{directory_css}

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
        "dateModified": "2026-11-24",
        "mainEntityOfPage": "https://smaranraut.com.np/blog/top-seo-experts-in-nepal/",
        "description": "A comprehensive directory and research guide reviewing the top SEO experts, consultants, and specialists in Nepal. Features verified profiles, core specialisations, agency affiliations, and hiring advice."
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
              <span class="item-desc">Explore all 28 in-depth SEO guides</span>
            </a>
            <div class="dropdown-divider"></div>
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
    <section class="hero-section" style="padding: 2.5rem 0 2rem; background: #0A1628; color: #FFFFFF;">
      <div class="container container-narrow">
        <div class="breadcrumbs" style="color: #94A3B8; margin-bottom: 1rem; font-size: 0.9rem;">
          <a href="../../index.html" style="color: #CBD5E1; text-decoration: none;">Home</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
          <a href="../index.html" style="color: #CBD5E1; text-decoration: none;">Knowledge Hub</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
          <span style="color: #FFFFFF;">Top SEO Experts in Nepal</span>
        </div>
        <div style="margin-bottom: 1rem;">
          <span class="badge badge-teal" style="background: #245037; color: #6EE7B7; padding: 0.35rem 0.75rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600;">Editorial Directory &middot; Updated November 2026</span>
        </div>
        <h1 class="hero-title" style="font-size: 2.5rem; font-weight: 800; color: #FFFFFF; line-height: 1.2; margin: 0 0 1rem 0;">Top SEO Experts in Nepal</h1>
        <p class="hero-subtitle" style="font-size: 1.15rem; color: #94A3B8; max-width: 750px; line-height: 1.6; margin: 0;">
          A research-backed reference directory of leading SEO professionals, search consultants, and digital specialists operating in Nepal.
        </p>
      </div>
    </section>

    <div class="container container-narrow" style="padding: 3.5rem 1.5rem;">
      <article class="article-body">
{article_body}
      </article>
    </div>
  </main>

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
            <li><a href="../website-setup-and-management/index.html">Website Setup &amp; Management</a></li>
            <li><a href="../seo-services-explained/index.html">SEO Services Explained</a></li>
            <li><a href="index.html">Top SEO Experts in Nepal</a></li>
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
wp_php = f'''<?php
// Blog Guide Part: Top SEO Experts in Nepal - Comprehensive Professional Directory
if (!defined('ABSPATH')) exit;
?>
{directory_css}
<main id="main-content">
  <section class="hero-section" style="padding: 2.5rem 0 2rem; background: #0A1628; color: #FFFFFF;">
    <div class="container container-narrow">
      <div class="breadcrumbs" style="color: #94A3B8; margin-bottom: 1rem; font-size: 0.9rem;">
        <a href="<?php echo esc_url(home_url('/')); ?>" style="color: #CBD5E1; text-decoration: none;">Home</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
        <a href="<?php echo esc_url(home_url('/blog/')); ?>" style="color: #CBD5E1; text-decoration: none;">Knowledge Hub</a> <span class="sep" style="margin: 0 0.5rem;">/</span> 
        <span style="color: #FFFFFF;">Top SEO Experts in Nepal</span>
      </div>
      <div style="margin-bottom: 1rem;">
        <span class="badge badge-teal" style="background: #245037; color: #6EE7B7; padding: 0.35rem 0.75rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600;">Editorial Directory &middot; Updated November 2026</span>
      </div>
      <h1 class="hero-title" style="font-size: 2.5rem; font-weight: 800; color: #FFFFFF; line-height: 1.2; margin: 0 0 1rem 0;">Top SEO Experts in Nepal</h1>
      <p class="hero-subtitle" style="font-size: 1.15rem; color: #94A3B8; max-width: 750px; line-height: 1.6; margin: 0;">
        A research-backed reference directory of leading SEO professionals, search consultants, and digital specialists operating in Nepal.
      </p>
    </div>
  </section>

  <div class="container container-narrow" style="padding: 3.5rem 1.5rem;">
    <article class="article-body">
{article_body}
    </article>
  </div>
</main>
'''

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Written HTML to {html_path} ({len(full_html)} chars)")

with open(wp_path, "w", encoding="utf-8") as f:
    f.write(wp_php)
print(f"Written WordPress template part to {wp_path} ({len(wp_php)} chars)")
