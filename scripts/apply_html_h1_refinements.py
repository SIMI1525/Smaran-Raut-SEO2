import os
import re

html_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"

html_replacements = {
    # Homepage
    r"index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Itahari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Itahari, Nepal</h1>'
    ),
    
    # 17 Location Pages
    r"seo-expert-belbari\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Belbari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Belbari, Nepal</h1>'
    ),
    r"seo-expert-biratnagar\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Biratnagar, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Biratnagar, Nepal</h1>'
    ),
    r"seo-expert-birtamod\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Birtamod, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Birtamod, Nepal</h1>'
    ),
    r"seo-expert-damak\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Damak, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Damak, Nepal</h1>'
    ),
    r"seo-expert-dhankuta\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Dhankuta, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Dhankuta, Nepal</h1>'
    ),
    r"seo-expert-dharan\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Dharan, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Dharan, Nepal</h1>'
    ),
    r"seo-expert-duhabi\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Duhabi, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Duhabi, Nepal</h1>'
    ),
    r"seo-expert-gaighat\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Gaighat, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Gaighat, Nepal</h1>'
    ),
    r"seo-expert-ilam\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Ilam, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Ilam, Nepal</h1>'
    ),
    r"seo-expert-inaruwa\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Inaruwa, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Inaruwa, Nepal</h1>'
    ),
    r"seo-expert-itahari\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Itahari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Itahari, Nepal</h1>'
    ),
    r"seo-expert-jhumka\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Jhumka, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Jhumka, Nepal</h1>'
    ),
    r"seo-expert-lahan\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Lahan, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Lahan, Nepal</h1>'
    ),
    r"seo-expert-rajbiraj\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Rajbiraj, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Rajbiraj, Nepal</h1>'
    ),
    r"seo-expert-ramdhuni\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Ramdhuni, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Ramdhuni, Nepal</h1>'
    ),
    r"seo-expert-rangeli\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Rangeli, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Rangeli, Nepal</h1>'
    ),
    r"seo-expert-urlabari\index.html": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Urlabari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Urlabari, Nepal</h1>'
    ),

    # Services
    r"services\seo-optimized-web-development\index.html": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Fast, SEO-Optimized <span class="highlight">Website Development</span> for Businesses in Nepal[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">SEO-Optimized <span class="highlight">Website Development</span></h1>'
    ),
    r"services\local-seo-itahari\index.html": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Local SEO & Google Business Profile Ranking in <span class="highlight">Itahari & Eastern Nepal</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Local SEO & <span class="highlight">Google Business Profile Optimization</span></h1>'
    ),
    r"services\technical-seo-audit\index.html": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?SEO Health Checks &amp; Ranking Fixes for <span class="highlight">Existing Websites</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Technical SEO Audits &amp; <span class="highlight">Search Optimization</span></h1>'
    ),
    r"services\core-web-vitals-speed\index.html": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Website Speed Optimization &amp; <span class="highlight">Ongoing Maintenance</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Website Speed Optimization &amp; <span class="highlight">Technical Maintenance</span></h1>'
    ),
    r"services\ecommerce-seo-nepal\index.html": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?E-Commerce SEO &amp; <span class="highlight">Online Store Optimization</span> in Nepal[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">E-Commerce SEO &amp; <span class="highlight">Store Optimization</span></h1>'
    ),
    r"services\enterprise-link-building\index.html": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Ongoing Website Management &amp; <span class="highlight">Search Visibility Growth</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Ongoing Website Management &amp; <span class="highlight">SEO Support</span></h1>'
    ),

    # Pages
    r"about-us\index.html": (
        r'<h1 class="hero-title">About Smaran Raut: Building Fast, Search-Friendly Websites for Nepali Businesses</h1>',
        r'<h1 class="hero-title">About Smaran Raut</h1>'
    ),
    r"contact-us\index.html": (
        r'<h1 class="hero-title">Get in Touch with Smaran Raut: We Are Here to Help</h1>',
        r'<h1 class="hero-title">Get in Touch with Smaran Raut</h1>'
    ),
    r"case-studies\index.html": (
        r'<h1 class="hero-title">Client Work Examples: Practical Website Solutions &amp; Search Growth</h1>',
        r'<h1 class="hero-title">Client Case Studies &amp; Search Results</h1>'
    ),
    r"consultation\index.html": (
        r'<h1 class="hero-title">Schedule a One-on-One Website &amp; SEO Strategy Consultation</h1>',
        r'<h1 class="hero-title">Schedule a Website &amp; SEO Consultation</h1>'
    ),
    r"office-location\index.html": (
        r'<h1 class="hero-title">Our Physical Office Location in Itahari, Sunsari</h1>',
        r'<h1 class="hero-title">Office Location in Itahari, Sunsari</h1>'
    ),

    # Blog Articles
    r"blog\cls-cumulative-layout-shift-fixes\index.html": (
        r'<h1 class="hero-title">How to Fix Cumulative Layout Shift \(CLS\) for a Flawless 0\.00 Score</h1>',
        r'<h1 class="hero-title">How to Fix Cumulative Layout Shift (CLS)</h1>'
    ),
    r"blog\competitor-backlink-gap-analysis\index.html": (
        r'<h1 class="hero-title">How to Reverse-Engineer Competitor Backlinks to Uncover Link Opportunities</h1>',
        r'<h1 class="hero-title">How to Conduct a Competitor Backlink Gap Analysis</h1>'
    ),
    r"blog\crawl-budget-optimization-large-sites\index.html": (
        r'<h1 class="hero-title">Crawl Budget Management: How to Help Googlebot Index High-Priority Pages</h1>',
        r'<h1 class="hero-title">Crawl Budget Optimization for Large Websites</h1>'
    ),
    r"blog\ecommerce-category-page-seo-strategy\index.html": (
        r'<h1 class="hero-title">How to Build High-Ranking E-Commerce Category & Collection Pages</h1>',
        r'<h1 class="hero-title">E-Commerce Category Page SEO Strategy</h1>'
    ),
    r"blog\fixing-canonical-tag-issues-pagination\index.html": (
        r'<h1 class="hero-title">Canonical Tag Troubleshooting: Avoiding Duplicate Content Penalties</h1>',
        r'<h1 class="hero-title">Canonical Tag Troubleshooting and Pagination Best Practices</h1>'
    ),
    r"blog\google-business-profile-optimization-nepal\index.html": (
        r'<h1 class="hero-title">How to Optimize Google Business Profile for #1 Ranking in Nepal</h1>',
        r'<h1 class="hero-title">How to Optimize Google Business Profile in Nepal</h1>'
    ),
    r"blog\how-seo-works\index.html": (
        r'<h1>How Does SEO Work\? Understanding Google\'s Ranking Algorithm in Nepal</h1>',
        r'<h1 class="hero-title">How Does SEO Work? Understanding Search Rankings</h1>'
    ),
    r"blog\how-to-conduct-technical-seo-audit\index.html": (
        r'<h1 class="hero-title">How to Perform an Enterprise Technical SEO Audit from Scratch</h1>',
        r'<h1 class="hero-title">How to Conduct a Technical SEO Audit</h1>'
    ),
    r"blog\how-to-update-decaying-content\index.html": (
        r'<h1 class="hero-title">How to Audit and Refresh Decaying Content to Reclaim Top Rankings</h1>',
        r'<h1 class="hero-title">How to Audit and Refresh Decaying Content</h1>'
    ),
    r"blog\image-compression-avif-webp-delivery\index.html": (
        r'<h1 class="hero-title">AVIF vs\. WebP Image Compression: Slashing Page Weight by 70%</h1>',
        r'<h1 class="hero-title">AVIF vs. WebP: Modern Image Compression for the Web</h1>'
    ),
    r"blog\inp-interaction-to-next-paint-guide\index.html": (
        r'<h1 class="hero-title">How to Debug and Optimize Interaction to Next Paint \(INP\) Under 200ms</h1>',
        r'<h1 class="hero-title">How to Debug and Optimize Interaction to Next Paint (INP)</h1>'
    ),
    r"blog\lcp-optimization-hero-images-fonts\index.html": (
        r'<h1 class="hero-title">How to Achieve Sub-1\.5s Largest Contentful Paint \(LCP\) on Mobile Devices</h1>',
        r'<h1 class="hero-title">How to Optimize Largest Contentful Paint (LCP) on Mobile</h1>'
    ),
    r"blog\local-citations-nap-consistency-guide\index.html": (
        r'<h1 class="hero-title">NAP Consistency & Local Directory Citations in Nepal: Complete Guide</h1>',
        r'<h1 class="hero-title">NAP Consistency and Local Directory Citations in Nepal</h1>'
    ),
    r"blog\local-seo-vs-organic-seo-differences\index.html": (
        r'<h1 class="hero-title">Local SEO vs\. Traditional Organic SEO: Which Drives Greater Revenue\?</h1>',
        r'<h1 class="hero-title">Local SEO vs. Organic SEO: Key Differences and Strategy</h1>'
    ),
    r"blog\nextjs-vs-wordpress-for-seo\index.html": (
        r'<h1 class="hero-title">Next\.js vs\. WordPress for SEO: Which Architecture Dominates in 2026\?</h1>',
        r'<h1 class="hero-title">Next.js vs. WordPress for SEO: Architecture Comparison</h1>'
    ),
    r"blog\schema-markup-implementation-guide\index.html": (
        r'<h1 class="hero-title">How to Implement Schema Markup \(JSON-LD\) for Local Businesses in Nepal</h1>',
        r'<h1 class="hero-title">Schema Markup (JSON-LD) Implementation Guide</h1>'
    ),
    r"blog\seo-services-explained\index.html": (
        r'<h1 class="hero-title">SEO Services Explained: What Each Service Does and How It Helps Your Business</h1>',
        r'<h1 class="hero-title">SEO Services Explained: Core Capabilities and Business Impact</h1>'
    ),
    r"blog\social-media-and-online-advertising\index.html": (
        r'<h1 class="hero-title">Social Media and Online Advertisement: How Digital Ad Networks, Paid Social, and Campaign Measurement Work</h1>',
        r'<h1 class="hero-title">Social Media and Online Advertising Guide</h1>'
    ),
    r"blog\static-site-generation-benefits-ranking\index.html": (
        r'<h1 class="hero-title">The SEO Power of Static Site Generation: Instant Delivery & Zero Downtime</h1>',
        r'<h1 class="hero-title">Static Site Generation for SEO: Benefits and Architecture</h1>'
    ),
    r"blog\topical-authority-clustering-framework\index.html": (
        r'<h1 class="hero-title">How to Build a Topical Authority Content Cluster That Outranks Big Brands</h1>',
        r'<h1 class="hero-title">How to Build a Topical Authority Content Cluster</h1>'
    ),
    r"blog\toxic-backlink-audit-disavow-guide\index.html": (
        r'<h1 class="hero-title">The Truth About Toxic Backlinks: When Should You Use the Disavow Tool\?</h1>',
        r'<h1 class="hero-title">Toxic Backlink Audits: When to Use the Google Disavow Tool</h1>'
    ),
    r"blog\website-setup-and-management\index.html": (
        r'<h1 class="hero-title">Website Setup &amp; Management: Plain-English Guide to Domains, Hosting, Launch &amp; Care</h1>',
        r'<h1 class="hero-title">Website Setup &amp; Management: Domains, Hosting, and Maintenance</h1>'
    ),
    r"blog\what-is-seo\index.html": (
        r'<h1>What Is SEO\? A Complete Beginner\'s Guide for Nepal Businesses \(2026\)</h1>',
        r'<h1 class="hero-title">What Is SEO? A Beginner\'s Guide to Search Optimization</h1>'
    ),
    r"blog\white-hat-link-building-tactics-2026\index.html": (
        r'<h1 class="hero-title">White-Hat Link Building Strategies That Withstand Google Algorithm Updates</h1>',
        r'<h1 class="hero-title">White-Hat Link Building Strategies and Best Practices</h1>'
    )
}

print(f"Total targeted HTML files: {len(html_replacements)}")

html_success = 0
for rel, (pattern, replacement) in html_replacements.items():
    file_path = os.path.join(html_dir, rel)
    if not os.path.exists(file_path):
        print(f"MISSING: {file_path}")
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, count = re.subn(pattern, replacement, content, count=1)
    if count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        html_success += 1
        print(f"[HTML OK] {rel}")
    else:
        print(f"[HTML FAIL MATCH] {rel}")

print(f"\nHTML files updated: {html_success}/{len(html_replacements)}")
