import os
import re

html_base = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
wp_base = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

# 1. how-seo-works
html_hsw = os.path.join(html_base, "blog", "how-seo-works", "index.html")
wp_hsw = os.path.join(wp_base, "template-parts", "blog", "how-seo-works.php")

with open(html_hsw, "r", encoding="utf-8") as f:
    c = f.read()

# Fix stacked heading 1
old_s1 = '<h2>The Three-Stage Google Process: Crawl → Index → Rank</h2>\n\n  <h3>Stage 1: Crawling'
new_s1 = '<h2>The Three-Stage Google Process: Crawl → Index → Rank</h2>\n  <p>Google ranks web pages through a sequential three-stage pipeline comprising automated crawling, database indexing, and algorithmic ranking to deliver relevant search results for user queries.</p>\n\n  <h3>Stage 1: Crawling'
if old_s1 in c:
    c = c.replace(old_s1, new_s1)

# Fix stacked heading 2
old_s2 = '<h2>Nepal-Specific Ranking Signals You Need to Understand</h2>\n\n  <h3>Google Business Profile'
new_s2 = '<h2>Nepal-Specific Ranking Signals You Need to Understand</h2>\n  <p>Ranking in Nepal requires search engines to evaluate distinct localized signals, including Google Business Profile proximity, regional entity authority, mobile page speed over local telecommunication networks, and localized content relevance.</p>\n\n  <h3>Google Business Profile'
if old_s2 in c:
    c = c.replace(old_s2, new_s2)

# Add supplementary section before cta-box or before </section>
hsw_supp_html = """
  <h2>Diagnosing Search Algorithm Bottlenecks on Existing Nepal Websites</h2>
  <p>
    While understanding crawl budgets, indexation rules, and algorithmic signals provides the theoretical foundation for search visibility, real-world websites often suffer from unseen code errors, slow server responses, and canonical conflicts. When search traffic plateaus despite consistent publishing, professional <a href="../../services/technical-seo-audit/index.html">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a> uncover exact indexing bottlenecks, isolate server configuration faults, and restore predictable ranking performance across competitive search queries.
  </p>
"""
if 'Diagnosing Search Algorithm Bottlenecks' not in c:
    target_pos = c.find('</section>\n\n  <div class="cta-box">')
    if target_pos != -1:
        c = c[:target_pos] + hsw_supp_html + c[target_pos:]

with open(html_hsw, "w", encoding="utf-8") as f:
    f.write(c)

# Mirror to WP
with open(wp_hsw, "r", encoding="utf-8") as f:
    w = f.read()

if old_s1 in w:
    w = w.replace(old_s1, new_s1)
if old_s2 in w:
    w = w.replace(old_s2, new_s2)

hsw_supp_wp = """
  <h2>Diagnosing Search Algorithm Bottlenecks on Existing Nepal Websites</h2>
  <p>
    While understanding crawl budgets, indexation rules, and algorithmic signals provides the theoretical foundation for search visibility, real-world websites often suffer from unseen code errors, slow server responses, and canonical conflicts. When search traffic plateaus despite consistent publishing, professional <a href="<?php echo esc_url(home_url('/services/technical-seo-audit/')); ?>">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a> uncover exact indexing bottlenecks, isolate server configuration faults, and restore predictable ranking performance across competitive search queries.
  </p>
"""
if 'Diagnosing Search Algorithm Bottlenecks' not in w:
    target_pos = w.find('</section>\n\n  <div class="cta-box">')
    if target_pos != -1:
        w = w[:target_pos] + hsw_supp_wp + w[target_pos:]

with open(wp_hsw, "w", encoding="utf-8") as f:
    f.write(w)

print("Updated how-seo-works in HTML and WP")

# 2. what-is-seo
html_wis = os.path.join(html_base, "blog", "what-is-seo", "index.html")
wp_wis = os.path.join(wp_base, "template-parts", "blog", "what-is-seo.php")

with open(html_wis, "r", encoding="utf-8") as f:
    c = f.read()

# Fix stacked headings in what-is-seo
old_w1 = '<h2>The 3 Pillars of SEO Every Nepal Business Owner Must Know</h2>\n\n  <div class="highlight-box">'
new_w1 = '<h2>The 3 Pillars of SEO Every Nepal Business Owner Must Know</h2>\n  <p>The three foundational pillars of search engine optimization are technical infrastructure, on-page content relevance, and off-page authority signals, which together determine a website\'s organic visibility in Google.</p>\n\n  <div class="highlight-box">'
if old_w1 in c:
    c = c.replace(old_w1, new_w1)

old_w2 = '<h2>Essential SEO Terms Explained for Nepal Business Owners</h2>\n\n  <h3>Keywords</h3>'
new_w2 = '<h2>Essential SEO Terms Explained for Nepal Business Owners</h2>\n  <p>Understanding core search optimization terminology allows business owners to interpret search performance reports, communicate effectively with technical specialists, and implement strategic digital marketing initiatives.</p>\n\n  <h3>Keywords</h3>'
if old_w2 in c:
    c = c.replace(old_w2, new_w2)

old_w3 = '<h2>Your First 5 SEO Steps as a Nepal Business Owner</h2>\n  <ol>'
new_w3 = '<h2>Your First 5 SEO Steps as a Nepal Business Owner</h2>\n  <p>Launching an effective search strategy begins with prioritizing local entity verification, fast technical infrastructure, and targeted content creation before scaling into complex competitive campaigns.</p>\n  <ol>'
if old_w3 in c:
    c = c.replace(old_w3, new_w3)

wis_supp_html = """
  <h2>Connecting Search Engine Visibility to Local Foot Traffic and Revenue</h2>
  <p>
    Learning the basic definitions of search engine optimization helps business owners recognize how organic search drives customer discovery across Nepal. However, translating search visibility into physical foot traffic, customer inquiries, and sustainable revenue requires localized geo-targeting and map optimization. For business owners seeking immediate local visibility across Koshi Province, implementing dedicated <a href="../../services/local-seo-itahari/index.html">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a> captures nearby commercial searches, improves Google Maps map-pack placement, and turns high-intent searchers into paying clients.
  </p>
"""
if 'Connecting Search Engine Visibility to Local Foot Traffic' not in c:
    target_pos = c.find('</section>\n\n  <div class="cta-box">')
    if target_pos != -1:
        c = c[:target_pos] + wis_supp_html + c[target_pos:]

with open(html_wis, "w", encoding="utf-8") as f:
    f.write(c)

with open(wp_wis, "r", encoding="utf-8") as f:
    w = f.read()

if old_w1 in w:
    w = w.replace(old_w1, new_w1)
if old_w2 in w:
    w = w.replace(old_w2, new_w2)
if old_w3 in w:
    w = w.replace(old_w3, new_w3)

wis_supp_wp = """
  <h2>Connecting Search Engine Visibility to Local Foot Traffic and Revenue</h2>
  <p>
    Learning the basic definitions of search engine optimization helps business owners recognize how organic search drives customer discovery across Nepal. However, translating search visibility into physical foot traffic, customer inquiries, and sustainable revenue requires localized geo-targeting and map optimization. For business owners seeking immediate local visibility across Koshi Province, implementing dedicated <a href="<?php echo esc_url(home_url('/services/local-seo-itahari/')); ?>">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a> captures nearby commercial searches, improves Google Maps map-pack placement, and turns high-intent searchers into paying clients.
  </p>
"""
if 'Connecting Search Engine Visibility to Local Foot Traffic' not in w:
    target_pos = w.find('</section>\n\n  <div class="cta-box">')
    if target_pos != -1:
        w = w[:target_pos] + wis_supp_wp + w[target_pos:]

with open(wp_wis, "w", encoding="utf-8") as f:
    f.write(w)

print("Updated what-is-seo in HTML and WP")

# 3. website-setup-and-management
html_wsm = os.path.join(html_base, "blog", "website-setup-and-management", "index.html")
wp_wsm = os.path.join(wp_base, "template-parts", "blog", "website-setup-and-management.php")

with open(html_wsm, "r", encoding="utf-8") as f:
    c = f.read()

wsm_supp_html = """
          <h2>Turning Website Setup Plans into High-Performance Digital Assets</h2>
          <p>
            While understanding domains, hosting, and technical configuration prevents costly administrative mistakes, deploying a secure, responsive business website requires specialized development practices. For enterprises and growing brands seeking turnkey execution, our <a href="../../services/seo-optimized-web-development/index.html">Fast, SEO-Optimized Website Development for Businesses in Nepal</a> practice engineers high-speed code architectures, integrates technical SEO foundations, and guarantees sub-second page delivery from day one.
          </p>
"""
if 'Turning Website Setup Plans into High-Performance' not in c:
    target_pos = c.find('<!-- Final Consultation Callout Box -->')
    if target_pos != -1:
        c = c[:target_pos] + wsm_supp_html + "\n          " + c[target_pos:]

with open(html_wsm, "w", encoding="utf-8") as f:
    f.write(c)

with open(wp_wsm, "r", encoding="utf-8") as f:
    w = f.read()

wsm_supp_wp = """
          <h2>Turning Website Setup Plans into High-Performance Digital Assets</h2>
          <p>
            While understanding domains, hosting, and technical configuration prevents costly administrative mistakes, deploying a secure, responsive business website requires specialized development practices. For enterprises and growing brands seeking turnkey execution, our <a href="<?php echo esc_url(home_url('/services/seo-optimized-web-development/')); ?>">Fast, SEO-Optimized Website Development for Businesses in Nepal</a> practice engineers high-speed code architectures, integrates technical SEO foundations, and guarantees sub-second page delivery from day one.
          </p>
"""
if 'Turning Website Setup Plans into High-Performance' not in w:
    target_pos = w.find('<!-- Final Consultation Callout Box -->')
    if target_pos != -1:
        w = w[:target_pos] + wsm_supp_wp + "\n          " + w[target_pos:]

with open(wp_wsm, "w", encoding="utf-8") as f:
    f.write(w)

print("Updated website-setup-and-management in HTML and WP")

# 4. seo-services-explained
html_sse = os.path.join(html_base, "blog", "seo-services-explained", "index.html")
wp_sse = os.path.join(wp_base, "template-parts", "blog", "seo-services-explained.php")

with open(html_sse, "r", encoding="utf-8") as f:
    c = f.read()

sse_supp_html = """
          <h2>Selecting the Right Search and Development Engagement for Your Business</h2>
          <p>
            Every commercial website presents unique growth bottlenecks, ranging from missing local map citations to severe technical crawl blocks or unoptimized page speeds. Rather than investing in fragmented tactics, reviewing our comprehensive <a href="../../services/index.html">Services Overview: Web Development &amp; SEO Packages</a> allows business owners to compare dedicated service scopes, understand deliverable timelines, and select an engagement model aligned directly with their current revenue goals.
          </p>
"""
if 'Selecting the Right Search and Development Engagement' not in c:
    target_pos = c.find('<!-- Final Consultation Callout Box -->')
    if target_pos != -1:
        c = c[:target_pos] + sse_supp_html + "\n          " + c[target_pos:]

with open(html_sse, "w", encoding="utf-8") as f:
    f.write(c)

with open(wp_sse, "r", encoding="utf-8") as f:
    w = f.read()

sse_supp_wp = """
          <h2>Selecting the Right Search and Development Engagement for Your Business</h2>
          <p>
            Every commercial website presents unique growth bottlenecks, ranging from missing local map citations to severe technical crawl blocks or unoptimized page speeds. Rather than investing in fragmented tactics, reviewing our comprehensive <a href="<?php echo esc_url(home_url('/services/')); ?>">Services Overview: Web Development &amp; SEO Packages</a> allows business owners to compare dedicated service scopes, understand deliverable timelines, and select an engagement model aligned directly with their current revenue goals.
          </p>
"""
if 'Selecting the Right Search and Development Engagement' not in w:
    target_pos = w.find('<!-- Final Consultation Callout Box -->')
    if target_pos != -1:
        w = w[:target_pos] + sse_supp_wp + "\n          " + w[target_pos:]

with open(wp_sse, "w", encoding="utf-8") as f:
    f.write(w)

print("Updated seo-services-explained in HTML and WP")

# 5. social-media-and-online-advertising
html_smoa = os.path.join(html_base, "blog", "social-media-and-online-advertising", "index.html")
wp_smoa = os.path.join(wp_base, "template-parts", "blog", "social-media-and-online-advertising.php")

with open(html_smoa, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    'Combining paid traffic campaigns with <a href="../../services/seo-optimized-web-development/index.html"><strong>SEO-Optimized Business Website Development</strong></a>',
    'Combining paid traffic campaigns with <a href="../../services/seo-optimized-web-development/index.html"><strong>Fast, SEO-Optimized Website Development for Businesses in Nepal</strong></a>'
)

with open(html_smoa, "w", encoding="utf-8") as f:
    f.write(c)

with open(wp_smoa, "r", encoding="utf-8") as f:
    w = f.read()

w = w.replace(
    'Combining paid traffic campaigns with <a href="<?php echo esc_url(home_url(\'/services/seo-optimized-web-development/\')); ?>"><strong>SEO-Optimized Business Website Development</strong></a>',
    'Combining paid traffic campaigns with <a href="<?php echo esc_url(home_url(\'/services/seo-optimized-web-development/\')); ?>"><strong>Fast, SEO-Optimized Website Development for Businesses in Nepal</strong></a>'
)

with open(wp_smoa, "w", encoding="utf-8") as f:
    f.write(w)

print("Updated social-media-and-online-advertising in HTML and WP")
