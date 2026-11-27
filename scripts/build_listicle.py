# Python script to build the complete listicle HTML and WordPress template
import os

html_output_path = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\top-seo-experts-in-nepal\index.html"
wp_output_path = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\top-seo-experts-in-nepal.php"

os.makedirs(os.path.dirname(html_output_path), exist_ok=True)
os.makedirs(os.path.dirname(wp_output_path), exist_ok=True)

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

def render_cards_html():
    html = ['<div class="directory-grid">']
    for p in profiles:
        company_tag = f'<span class="profile-company">{p["company"]}</span>' if p["company"] else ''
        specs_list = ''.join([f'<li class="spec-item"><span class="spec-dot"></span>{s}</li>' for s in p["specs"]])
        
        links = []
        if p["website"]:
            links.append(f'<a href="{p["website"]}" target="_blank" rel="noopener noreferrer" class="profile-link profile-link--web"><svg class="link-icon" viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>Website</a>')
        if p.get("linkedin"):
            links.append(f'<a href="{p["linkedin"]}" target="_blank" rel="noopener noreferrer" class="profile-link profile-link--linkedin"><svg class="link-icon" viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>LinkedIn</a>')
        if p.get("gbp"):
            links.append(f'<a href="{p["gbp"]}" target="_blank" rel="noopener noreferrer" class="profile-link profile-link--gbp"><svg class="link-icon" viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>Google Business Profile</a>')
            
        links_html = '<div class="profile-links">' + ''.join(links) + '</div>'
        
        card = f'''
        <article class="directory-card" id="{p["name"].lower().replace(' ', '-').replace('.', '')}">
          <div class="profile-header">
            <div class="profile-avatar" aria-hidden="true">{p["initials"]}</div>
            <div class="profile-meta">
              <h3 class="profile-name">{p["name"]}</h3>
              <div class="profile-title">{p["title"]}</div>
              <div class="profile-location">
                <svg class="loc-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                <span>{p["location"]}</span>
                {company_tag}
              </div>
            </div>
          </div>
          <p class="profile-desc">{p["desc"]}</p>
          <div class="profile-specs-wrapper">
            <span class="specs-heading">Key Specialisations:</span>
            <ul class="profile-specs">
              {specs_list}
            </ul>
          </div>
          {links_html}
        </article>
        '''
        html.append(card)
    html.append('</div>')
    return '\n'.join(html)

print("Card renderer prepared. Total profiles:", len(profiles))
