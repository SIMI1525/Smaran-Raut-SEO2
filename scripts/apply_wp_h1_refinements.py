import os
import re

wp_theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"
html_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"

# Define the exact mapping of relative file paths and their H1 replacements
# For WordPress PHP files:
wp_replacements = {
    # Homepage Hero
    r"template-parts\hero.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Itahari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Itahari, Nepal</h1>'
    ),
    
    # 17 Location Pages
    r"template-parts\geo\belbari.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Belbari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Belbari, Nepal</h1>'
    ),
    r"template-parts\geo\biratnagar.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Biratnagar, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Biratnagar, Nepal</h1>'
    ),
    r"template-parts\geo\birtamod.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Birtamod, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Birtamod, Nepal</h1>'
    ),
    r"template-parts\geo\damak.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Damak, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Damak, Nepal</h1>'
    ),
    r"template-parts\geo\dhankuta.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Dhankuta, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Dhankuta, Nepal</h1>'
    ),
    r"template-parts\geo\dharan.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Dharan, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Dharan, Nepal</h1>'
    ),
    r"template-parts\geo\duhabi.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Duhabi, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Duhabi, Nepal</h1>'
    ),
    r"template-parts\geo\gaighat.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Gaighat, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Gaighat, Nepal</h1>'
    ),
    r"template-parts\geo\ilam.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Ilam, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Ilam, Nepal</h1>'
    ),
    r"template-parts\geo\inaruwa.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Inaruwa, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Inaruwa, Nepal</h1>'
    ),
    r"template-parts\geo\itahari.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Itahari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Itahari, Nepal</h1>'
    ),
    r"template-parts\geo\jhumka.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Jhumka, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Jhumka, Nepal</h1>'
    ),
    r"template-parts\geo\lahan.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Lahan, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Lahan, Nepal</h1>'
    ),
    r"template-parts\geo\rajbiraj.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Rajbiraj, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Rajbiraj, Nepal</h1>'
    ),
    r"template-parts\geo\ramdhuni.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Ramdhuni, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Ramdhuni, Nepal</h1>'
    ),
    r"template-parts\geo\rangeli.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Rangeli, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Rangeli, Nepal</h1>'
    ),
    r"template-parts\geo\urlabari.php": (
        r'<h1 class="hero-title">\s*No\.1 SEO Expert in Urlabari, Nepal - Smaran Raut\s*</h1>',
        r'<h1 class="hero-title">SEO Expert in Urlabari, Nepal</h1>'
    ),

    # Services
    r"template-parts\services\seo-optimized-web-development.php": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Fast, SEO-Optimized <span class="highlight">Website Development</span> for Businesses in Nepal[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">SEO-Optimized <span class="highlight">Website Development</span></h1>'
    ),
    r"template-parts\services\local-seo-itahari.php": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Local SEO & Google Business Profile Ranking in <span class="highlight">Itahari & Eastern Nepal</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Local SEO & <span class="highlight">Google Business Profile Optimization</span></h1>'
    ),
    r"template-parts\services\technical-seo-audit.php": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?SEO Health Checks &amp; Ranking Fixes for <span class="highlight">Existing Websites</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Technical SEO Audits &amp; <span class="highlight">Search Optimization</span></h1>'
    ),
    r"template-parts\services\core-web-vitals-speed.php": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Website Speed Optimization &amp; <span class="highlight">Ongoing Maintenance</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Website Speed Optimization &amp; <span class="highlight">Technical Maintenance</span></h1>'
    ),
    r"template-parts\services\ecommerce-seo-nepal.php": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?E-Commerce SEO &amp; <span class="highlight">Online Store Optimization</span> in Nepal[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">E-Commerce SEO &amp; <span class="highlight">Store Optimization</span></h1>'
    ),
    r"template-parts\services\enterprise-link-building.php": (
        r'<h1 class="hero-title"[^>]*>[\s\S]*?Ongoing Website Management &amp; <span class="highlight">Search Visibility Growth</span>[\s\S]*?</h1>',
        r'<h1 class="hero-title" style="max-width: 950px;">Ongoing Website Management &amp; <span class="highlight">SEO Support</span></h1>'
    ),

    # Pages
    r"template-parts\pages\about-us.php": (
        r'<h1 class="hero-title">About Smaran Raut: Building Fast, Search-Friendly Websites for Nepali Businesses</h1>',
        r'<h1 class="hero-title">About Smaran Raut</h1>'
    ),
    r"template-parts\pages\contact-us.php": (
        r'<h1 class="hero-title">Get in Touch with Smaran Raut: We Are Here to Help</h1>',
        r'<h1 class="hero-title">Get in Touch with Smaran Raut</h1>'
    ),
    r"template-parts\pages\case-studies.php": (
        r'<h1 class="hero-title">Client Work Examples: Practical Website Solutions &amp; Search Growth</h1>',
        r'<h1 class="hero-title">Client Case Studies &amp; Search Results</h1>'
    ),
    r"template-parts\pages\consultation.php": (
        r'<h1 class="hero-title">Schedule a One-on-One Website &amp; SEO Strategy Consultation</h1>',
        r'<h1 class="hero-title">Schedule a Website &amp; SEO Consultation</h1>'
    ),
    r"template-parts\pages\office-location.php": (
        r'<h1 class="hero-title">Our Physical Office Location in Itahari, Sunsari</h1>',
        r'<h1 class="hero-title">Office Location in Itahari, Sunsari</h1>'
    ),

    # Blog Articles
    r"template-parts\blog\cls-cumulative-layout-shift-fixes.php": (
        r'<h1 class="hero-title">How to Fix Cumulative Layout Shift \(CLS\) for a Flawless 0\.00 Score</h1>',
        r'<h1 class="hero-title">How to Fix Cumulative Layout Shift (CLS)</h1>'
    ),
    r"template-parts\blog\competitor-backlink-gap-analysis.php": (
        r'<h1 class="hero-title">How to Reverse-Engineer Competitor Backlinks to Uncover Link Opportunities</h1>',
        r'<h1 class="hero-title">How to Conduct a Competitor Backlink Gap Analysis</h1>'
    ),
    r"template-parts\blog\crawl-budget-optimization-large-sites.php": (
        r'<h1 class="hero-title">Crawl Budget Management: How to Help Googlebot Index High-Priority Pages</h1>',
        r'<h1 class="hero-title">Crawl Budget Optimization for Large Websites</h1>'
    ),
    r"template-parts\blog\ecommerce-category-page-seo-strategy.php": (
        r'<h1 class="hero-title">How to Build High-Ranking E-Commerce Category & Collection Pages</h1>',
        r'<h1 class="hero-title">E-Commerce Category Page SEO Strategy</h1>'
    ),
    r"template-parts\blog\fixing-canonical-tag-issues-pagination.php": (
        r'<h1 class="hero-title">Canonical Tag Troubleshooting: Avoiding Duplicate Content Penalties</h1>',
        r'<h1 class="hero-title">Canonical Tag Troubleshooting and Pagination Best Practices</h1>'
    ),
    r"template-parts\blog\google-business-profile-optimization-nepal.php": (
        r'<h1 class="hero-title">How to Optimize Google Business Profile for #1 Ranking in Nepal</h1>',
        r'<h1 class="hero-title">How to Optimize Google Business Profile in Nepal</h1>'
    ),
    r"template-parts\blog\how-seo-works.php": (
        r'<h1>How Does SEO Work\? Understanding Google\'s Ranking Algorithm in Nepal</h1>',
        r'<h1 class="hero-title">How Does SEO Work? Understanding Search Rankings</h1>'
    ),
    r"template-parts\blog\how-to-conduct-technical-seo-audit.php": (
        r'<h1 class="hero-title">How to Perform an Enterprise Technical SEO Audit from Scratch</h1>',
        r'<h1 class="hero-title">How to Conduct a Technical SEO Audit</h1>'
    ),
    r"template-parts\blog\how-to-update-decaying-content.php": (
        r'<h1 class="hero-title">How to Audit and Refresh Decaying Content to Reclaim Top Rankings</h1>',
        r'<h1 class="hero-title">How to Audit and Refresh Decaying Content</h1>'
    ),
    r"template-parts\blog\image-compression-avif-webp-delivery.php": (
        r'<h1 class="hero-title">AVIF vs\. WebP Image Compression: Slashing Page Weight by 70%</h1>',
        r'<h1 class="hero-title">AVIF vs. WebP: Modern Image Compression for the Web</h1>'
    ),
    r"template-parts\blog\inp-interaction-to-next-paint-guide.php": (
        r'<h1 class="hero-title">How to Debug and Optimize Interaction to Next Paint \(INP\) Under 200ms</h1>',
        r'<h1 class="hero-title">How to Debug and Optimize Interaction to Next Paint (INP)</h1>'
    ),
    r"template-parts\blog\lcp-optimization-hero-images-fonts.php": (
        r'<h1 class="hero-title">How to Achieve Sub-1\.5s Largest Contentful Paint \(LCP\) on Mobile Devices</h1>',
        r'<h1 class="hero-title">How to Optimize Largest Contentful Paint (LCP) on Mobile</h1>'
    ),
    r"template-parts\blog\local-citations-nap-consistency-guide.php": (
        r'<h1 class="hero-title">NAP Consistency & Local Directory Citations in Nepal: Complete Guide</h1>',
        r'<h1 class="hero-title">NAP Consistency and Local Directory Citations in Nepal</h1>'
    ),
    r"template-parts\blog\local-seo-vs-organic-seo-differences.php": (
        r'<h1 class="hero-title">Local SEO vs\. Traditional Organic SEO: Which Drives Greater Revenue\?</h1>',
        r'<h1 class="hero-title">Local SEO vs. Organic SEO: Key Differences and Strategy</h1>'
    ),
    r"template-parts\blog\nextjs-vs-wordpress-for-seo.php": (
        r'<h1 class="hero-title">Next\.js vs\. WordPress for SEO: Which Architecture Dominates in 2026\?</h1>',
        r'<h1 class="hero-title">Next.js vs. WordPress for SEO: Architecture Comparison</h1>'
    ),
    r"template-parts\blog\schema-markup-implementation-guide.php": (
        r'<h1 class="hero-title">How to Implement Schema Markup \(JSON-LD\) for Local Businesses in Nepal</h1>',
        r'<h1 class="hero-title">Schema Markup (JSON-LD) Implementation Guide</h1>'
    ),
    r"template-parts\blog\seo-services-explained.php": (
        r'<h1 class="hero-title">SEO Services Explained: What Each Service Does and How It Helps Your Business</h1>',
        r'<h1 class="hero-title">SEO Services Explained: Core Capabilities and Business Impact</h1>'
    ),
    r"template-parts\blog\social-media-and-online-advertising.php": (
        r'<h1 class="hero-title">Social Media and Online Advertisement: How Digital Ad Networks, Paid Social, and Campaign Measurement Work</h1>',
        r'<h1 class="hero-title">Social Media and Online Advertising Guide</h1>'
    ),
    r"template-parts\blog\static-site-generation-benefits-ranking.php": (
        r'<h1 class="hero-title">The SEO Power of Static Site Generation: Instant Delivery & Zero Downtime</h1>',
        r'<h1 class="hero-title">Static Site Generation for SEO: Benefits and Architecture</h1>'
    ),
    r"template-parts\blog\topical-authority-clustering-framework.php": (
        r'<h1 class="hero-title">How to Build a Topical Authority Content Cluster That Outranks Big Brands</h1>',
        r'<h1 class="hero-title">How to Build a Topical Authority Content Cluster</h1>'
    ),
    r"template-parts\blog\toxic-backlink-audit-disavow-guide.php": (
        r'<h1 class="hero-title">The Truth About Toxic Backlinks: When Should You Use the Disavow Tool\?</h1>',
        r'<h1 class="hero-title">Toxic Backlink Audits: When to Use the Google Disavow Tool</h1>'
    ),
    r"template-parts\blog\website-setup-and-management.php": (
        r'<h1 class="hero-title">Website Setup &amp; Management: Plain-English Guide to Domains, Hosting, Launch &amp; Care</h1>',
        r'<h1 class="hero-title">Website Setup &amp; Management: Domains, Hosting, and Maintenance</h1>'
    ),
    r"template-parts\blog\what-is-seo.php": (
        r'<h1>What Is SEO\? A Complete Beginner\'s Guide for Nepal Businesses \(2026\)</h1>',
        r'<h1 class="hero-title">What Is SEO? A Beginner\'s Guide to Search Optimization</h1>'
    ),
    r"template-parts\blog\white-hat-link-building-tactics-2026.php": (
        r'<h1 class="hero-title">White-Hat Link Building Strategies That Withstand Google Algorithm Updates</h1>',
        r'<h1 class="hero-title">White-Hat Link Building Strategies and Best Practices</h1>'
    )
}

print(f"Total targeted WordPress files: {len(wp_replacements)}")

wp_success = 0
for rel, (pattern, replacement) in wp_replacements.items():
    file_path = os.path.join(wp_theme_dir, rel)
    if not os.path.exists(file_path):
        print(f"MISSING: {file_path}")
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, count = re.subn(pattern, replacement, content, count=1)
    if count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        wp_success += 1
        print(f"[WP OK] {rel}")
    else:
        print(f"[WP FAIL MATCH] {rel}")

print(f"\nWordPress files updated: {wp_success}/{len(wp_replacements)}")
