import os
import re

html_base = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services"
wp_base = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\services"

blog_h1s = {
    "anchor-text-distribution-best-practices": "Anchor Text Optimization: Natural Ratios and Algorithmic Safety",
    "cls-cumulative-layout-shift-fixes": "How to Fix Cumulative Layout Shift (CLS) for a Flawless 0.00 Score",
    "competitor-backlink-gap-analysis": "How to Reverse-Engineer Competitor Backlinks to Uncover Link Opportunities",
    "crawl-budget-optimization-large-sites": "Crawl Budget Management: How to Help Googlebot Index High-Priority Pages",
    "ecommerce-category-page-seo-strategy": "How to Build High-Ranking E-Commerce Category & Collection Pages",
    "ecommerce-product-schema-rich-snippets": "Product Schema Implementation for Google Search & Shopping Snippets",
    "entity-based-seo-google-knowledge-graph": "Entity SEO: Aligning Your Content with the Google Knowledge Graph",
    "fixing-canonical-tag-issues-pagination": "Canonical Tag Troubleshooting: Avoiding Duplicate Content Penalties",
    "google-business-profile-optimization-nepal": "How to Optimize Google Business Profile for #1 Ranking in Nepal",
    "handling-faceted-navigation-duplicate-content": "Solving Faceted Navigation & Parameter Duplication in E-Commerce SEO",
    "how-seo-works": "How Does SEO Work? Understanding Google's Ranking Algorithm in Nepal",
    "how-to-conduct-technical-seo-audit": "How to Perform an Enterprise Technical SEO Audit from Scratch",
    "how-to-update-decaying-content": "How to Audit and Refresh Decaying Content to Reclaim Top Rankings",
    "https-ssl-security-seo-impact": "HTTPS, HSTS & Modern Web Security as Google Ranking Signals",
    "image-compression-avif-webp-delivery": "AVIF vs. WebP Image Compression: Slashing Page Weight by 70%",
    "inp-interaction-to-next-paint-guide": "How to Debug and Optimize Interaction to Next Paint (INP) Under 200ms",
    "lcp-optimization-hero-images-fonts": "How to Achieve Sub-1.5s Largest Contentful Paint (LCP) on Mobile Devices",
    "local-citations-nap-consistency-guide": "NAP Consistency & Local Directory Citations in Nepal: Complete Guide",
    "local-seo-vs-organic-seo-differences": "Local SEO vs. Traditional Organic SEO: Which Drives Greater Revenue?",
    "mobile-first-responsive-design-checklist": "Mobile-First Design Checklist for Google Indexing & Conversion Rate",
    "multi-location-seo-eastern-nepal": "Scaling Multi-Location SEO Across Itahari, Dharan, and Biratnagar",
    "nextjs-vs-wordpress-for-seo": "Next.js vs. WordPress for SEO: Which Architecture Dominates in 2026?",
    "optimizing-shopify-woocommerce-performance": "Speed Optimization Playbook for Shopify and WooCommerce Stores",
    "schema-markup-implementation-guide": "How to Implement Schema Markup (JSON-LD) for Local Businesses in Nepal",
    "search-intent-matching-content-briefs": "Search Intent Classification: Informational, Commercial & Transactional",
    "seo-services-explained": "SEO Services Explained: What Each Service Does and How It Helps Your Business",
    "social-media-and-online-advertising": "Social Media and Online Advertisement: How Digital Ad Networks, Paid Social, and Campaign Measurement Work",
    "static-site-generation-benefits-ranking": "The SEO Power of Static Site Generation: Instant Delivery & Zero Downtime",
    "topical-authority-clustering-framework": "How to Build a Topical Authority Content Cluster That Outranks Big Brands",
    "toxic-backlink-audit-disavow-guide": "The Truth About Toxic Backlinks: When Should You Use the Disavow Tool?",
    "website-setup-and-management": "Website Setup & Management: Plain-English Guide to Domains, Hosting, Launch & Care",
    "what-is-seo": "What Is SEO? A Complete Beginner's Guide for Nepal Businesses (2026)",
    "white-hat-link-building-tactics-2026": "White-Hat Link Building Strategies That Withstand Google Algorithm Updates"
}

service_slugs = [
    "core-web-vitals-speed",
    "ecommerce-seo-nepal",
    "enterprise-link-building",
    "local-seo-itahari",
    "semantic-content-strategy",
    "seo-optimized-web-development",
    "technical-seo-audit"
]

def update_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = []
    mod = False
    for line in lines:
        if 'blog/' in line and '<strong>' in line and '&mdash;' in line:
            # find slug
            m = re.search(r'blog/([^/]+)/index\.html', line)
            if m:
                slug = m.group(1)
                if slug in blog_h1s:
                    target_h1 = blog_h1s[slug].replace('&', '&amp;')
                    # replace inside <strong>...</strong>
                    line_new = re.sub(r'<strong>.*?</strong>', f'<strong>{target_h1}</strong>', line)
                    if line_new != line:
                        line = line_new
                        mod = True
        new_lines.append(line)
    if mod:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Updated HTML: {os.path.basename(os.path.dirname(filepath))}")

def update_wp(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = []
    mod = False
    for line in lines:
        if 'home_url(\'/blog/' in line and '<strong>' in line and '&mdash;' in line:
            m = re.search(r'home_url\(\'/blog/([^/]+)/\'\)', line)
            if m:
                slug = m.group(1)
                if slug in blog_h1s:
                    target_h1 = blog_h1s[slug].replace('&', '&amp;')
                    line_new = re.sub(r'<strong>.*?</strong>', f'<strong>{target_h1}</strong>', line)
                    if line_new != line:
                        line = line_new
                        mod = True
        new_lines.append(line)
    if mod:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Updated WP: {os.path.basename(filepath)}")

for slug in service_slugs:
    h_file = os.path.join(html_base, slug, "index.html")
    w_file = os.path.join(wp_base, f"{slug}.php")
    if os.path.exists(h_file):
        update_html(h_file)
    if os.path.exists(w_file):
        update_wp(w_file)
