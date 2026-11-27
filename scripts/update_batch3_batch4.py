import os
import glob
import re

html_base = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
wp_base = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

print("--- Updating Batch 3: 17 Geo Landing Pages ---")

geo_dirs = glob.glob(os.path.join(html_base, "seo-expert-*"))
print(f"Found {len(geo_dirs)} geo directories")

for gdir in geo_dirs:
    slug = os.path.basename(gdir) # e.g. seo-expert-biratnagar
    city = slug.replace("seo-expert-", "")
    html_file = os.path.join(gdir, "index.html")
    wp_file = os.path.join(wp_base, "template-parts", "geo", f"{city}.php")

    # 1. Update HTML
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            c = f.read()

        # Step 2
        old_p2 = '<p class="process-step-desc">We identify page speed issues, mobile usability flaws, and missing directory citations.</p>'
        new_p2 = '<p class="process-step-desc">We identify page speed issues, mobile usability flaws, and missing directory citations through <a href="../services/technical-seo-audit/index.html">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a>.</p>'
        if old_p2 in c:
            c = c.replace(old_p2, new_p2)

        # Step 3
        old_p3 = '<p class="process-step-desc">We add Schema structured data, optimize localized keywords, and verify your Google Business Profile.</p>'
        new_p3 = '<p class="process-step-desc">We add Schema structured data, optimize localized keywords, and verify your Google Business Profile with <a href="../services/local-seo-itahari/index.html">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a>.</p>'
        if old_p3 in c:
            c = c.replace(old_p3, new_p3)

        # FAQ Question 2
        # Match pattern: "No. My physical office is located at Itahari Chowk, middle of Janta Galli, Itahari. I serve businesses in ... as part of my regional service coverage across Eastern Nepal."
        pattern_faq2 = re.compile(r'No\. My physical office is located at Itahari Chowk, middle of Janta Galli, Itahari\.\s*I serve businesses in ([^<]+) as part of my regional service coverage across Eastern Nepal\.')
        repl_faq2 = r'No. My physical office is located at Itahari Chowk, middle of Janta Galli, Itahari (<a href="../office-location/index.html">Office Location: Physical Address &amp; Service Coverage</a>). I serve businesses in \1 as part of my regional service coverage across Eastern Nepal through dedicated <a href="../services/local-seo-itahari/index.html">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a>.'
        c = pattern_faq2.sub(repl_faq2, c)

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(c)

    # 2. Update WP
    if os.path.exists(wp_file):
        with open(wp_file, "r", encoding="utf-8") as f:
            w = f.read()

        old_p2_wp = '<p class="process-step-desc">We identify page speed issues, mobile usability flaws, and missing directory citations.</p>'
        new_p2_wp = '<p class="process-step-desc">We identify page speed issues, mobile usability flaws, and missing directory citations through <a href="<?php echo esc_url(home_url(\'/services/technical-seo-audit/\')); ?>">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a>.</p>'
        if old_p2_wp in w:
            w = w.replace(old_p2_wp, new_p2_wp)

        old_p3_wp = '<p class="process-step-desc">We add Schema structured data, optimize localized keywords, and verify your Google Business Profile.</p>'
        new_p3_wp = '<p class="process-step-desc">We add Schema structured data, optimize localized keywords, and verify your Google Business Profile with <a href="<?php echo esc_url(home_url(\'/services/local-seo-itahari/\')); ?>">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a>.</p>'
        if old_p3_wp in w:
            w = w.replace(old_p3_wp, new_p3_wp)

        pattern_faq2_wp = re.compile(r'No\. My physical office is located at Itahari Chowk, middle of Janta Galli, Itahari\.\s*I serve businesses in ([^<]+) as part of my regional service coverage across Eastern Nepal\.')
        repl_faq2_wp = r'No. My physical office is located at Itahari Chowk, middle of Janta Galli, Itahari (<a href="<?php echo esc_url(home_url(\'/office-location/\')); ?>">Office Location: Physical Address &amp; Service Coverage</a>). I serve businesses in \1 as part of my regional service coverage across Eastern Nepal through dedicated <a href="<?php echo esc_url(home_url(\'/services/local-seo-itahari/\')); ?>">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a>.'
        w = pattern_faq2_wp.sub(repl_faq2_wp, w)

        with open(wp_file, "w", encoding="utf-8") as f:
            f.write(w)

print("Updated 17 geo landing pages in both HTML and WP")

print("--- Updating Homepage (index.html & services-grid.php) ---")
# Homepage HTML
hp_file = os.path.join(html_base, "index.html")
with open(hp_file, "r", encoding="utf-8") as f:
    h = f.read()

# Service 1
old_s1 = '<p>We build custom business websites designed specifically for search engines and mobile devices. Every site features fast loading speeds, structured data, and easy-to-use inquiry forms.</p>'
new_s1 = '<p>We build custom business websites designed specifically for search engines and mobile devices through our <a href="services/seo-optimized-web-development/index.html">Fast, SEO-Optimized Website Development for Businesses in Nepal</a> practice. Every site features fast loading speeds, structured data, and easy-to-use inquiry forms.</p>'
if old_s1 in h:
    h = h.replace(old_s1, new_s1)

# Service 2
old_s2 = '<p>We optimize local search signals so nearby customers discover your physical storefront, clinic, or service business on Google Search and Google Maps.</p>'
new_s2 = '<p>We optimize local search signals through <a href="services/local-seo-itahari/index.html">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a> so nearby customers discover your physical storefront, clinic, or service business on Google Search and Google Maps.</p>'
if old_s2 in h:
    h = h.replace(old_s2, new_s2)

# Service 3
old_s3 = '<p>We conduct comprehensive diagnostic audits to find hidden technical errors, indexing bottlenecks, and code issues that stop existing websites from ranking.</p>'
new_s3 = '<p>We conduct comprehensive diagnostic audits with <a href="services/technical-seo-audit/index.html">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a> to find hidden technical errors, indexing bottlenecks, and code issues that stop existing websites from ranking.</p>'
if old_s3 in h:
    h = h.replace(old_s3, new_s3)

# Service 4
old_s4 = '<p>We optimize Core Web Vitals, compress code, and provide ongoing technical maintenance so your website remains fast, secure, and competitive in search results.</p>'
new_s4 = '<p>We maximize search retention and technical health through <a href="services/core-web-vitals-speed/index.html">Website Speed Optimization &amp; Ongoing Maintenance</a> so your website remains fast, secure, and competitive in search results.</p>'
if old_s4 in h:
    h = h.replace(old_s4, new_s4)

with open(hp_file, "w", encoding="utf-8") as f:
    f.write(h)

# WP services-grid.php
sg_file = os.path.join(wp_base, "template-parts", "services-grid.php")
with open(sg_file, "r", encoding="utf-8") as f:
    sg = f.read()

new_s1_wp = '<p>We build custom business websites designed specifically for search engines and mobile devices through our <a href="<?php echo esc_url(home_url(\'/services/seo-optimized-web-development/\')); ?>">Fast, SEO-Optimized Website Development for Businesses in Nepal</a> practice. Every site features fast loading speeds, structured data, and easy-to-use inquiry forms.</p>'
if old_s1 in sg:
    sg = sg.replace(old_s1, new_s1_wp)

new_s2_wp = '<p>We optimize local search signals through <a href="<?php echo esc_url(home_url(\'/services/local-seo-itahari/\')); ?>">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a> so nearby customers discover your physical storefront, clinic, or service business on Google Search and Google Maps.</p>'
if old_s2 in sg:
    sg = sg.replace(old_s2, new_s2_wp)

new_s3_wp = '<p>We conduct comprehensive diagnostic audits with <a href="<?php echo esc_url(home_url(\'/services/technical-seo-audit/\')); ?>">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a> to find hidden technical errors, indexing bottlenecks, and code issues that stop existing websites from ranking.</p>'
if old_s3 in sg:
    sg = sg.replace(old_s3, new_s3_wp)

new_s4_wp = '<p>We maximize search retention and technical health through <a href="<?php echo esc_url(home_url(\'/services/core-web-vitals-speed/\')); ?>">Website Speed Optimization &amp; Ongoing Maintenance</a> so your website remains fast, secure, and competitive in search results.</p>'
if old_s4 in sg:
    sg = sg.replace(old_s4, new_s4_wp)

with open(sg_file, "w", encoding="utf-8") as f:
    f.write(sg)

print("Updated Homepage in HTML and WP")

print("--- Updating Services Overview (services/index.html & page-services.php) ---")
so_html = os.path.join(html_base, "services", "index.html")
so_wp = os.path.join(wp_base, "page-services.php")

with open(so_html, "r", encoding="utf-8") as f:
    so = f.read()

old_pkg1_item = '<span>Website Design &amp; Development</span>'
new_pkg1_item = '<a href="seo-optimized-web-development/index.html" class="term-link">Fast, SEO-Optimized Website Development for Businesses in Nepal</a>'
if old_pkg1_item in so:
    so = so.replace(old_pkg1_item, new_pkg1_item)

old_pkg4_check = '<a href="../blog/seo-services-explained/index.html#technical-seo-check" class="term-link">Technical SEO Check</a>'
new_pkg4_check = '<a href="technical-seo-audit/index.html" class="term-link">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a>'
if old_pkg4_check in so:
    so = so.replace(old_pkg4_check, new_pkg4_check)

with open(so_html, "w", encoding="utf-8") as f:
    f.write(so)

with open(so_wp, "r", encoding="utf-8") as f:
    sowp = f.read()

new_pkg1_item_wp = '<a href="<?php echo esc_url(home_url(\'/services/seo-optimized-web-development/\')); ?>" class="term-link">Fast, SEO-Optimized Website Development for Businesses in Nepal</a>'
if old_pkg1_item in sowp:
    sowp = sowp.replace(old_pkg1_item, new_pkg1_item_wp)

new_pkg4_check_wp = '<a href="<?php echo esc_url(home_url(\'/services/technical-seo-audit/\')); ?>" class="term-link">SEO Health Checks &amp; Ranking Fixes for Existing Websites</a>'
if old_pkg4_check in sowp:
    sowp = sowp.replace(old_pkg4_check, new_pkg4_check_wp)

with open(so_wp, "w", encoding="utf-8") as f:
    f.write(sowp)

print("Updated Services Overview in HTML and WP")

print("--- Updating Batch 4: Core & Supporting Pages ---")
# office-location
ol_html = os.path.join(html_base, "office-location", "index.html")
ol_wp = os.path.join(wp_base, "template-parts", "pages", "office-location.php")

with open(ol_html, "r", encoding="utf-8") as f:
    ol = f.read()

old_ol = 'While our physical office is centered in Itahari at the transport crossroads of Eastern Nepal, we work with businesses throughout:'
new_ol = 'While our physical office is centered in Itahari at the transport crossroads of Eastern Nepal, we deliver targeted <a href="../services/local-seo-itahari/index.html">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a> for storefronts, clinics, and commercial enterprises throughout:'
if old_ol in ol:
    ol = ol.replace(old_ol, new_ol)

with open(ol_html, "w", encoding="utf-8") as f:
    f.write(ol)

with open(ol_wp, "r", encoding="utf-8") as f:
    olwp = f.read()

new_ol_wp = 'While our physical office is centered in Itahari at the transport crossroads of Eastern Nepal, we deliver targeted <a href="<?php echo esc_url(home_url(\'/services/local-seo-itahari/\')); ?>">Local SEO &amp; Google Business Profile Ranking in Itahari &amp; Eastern Nepal</a> for storefronts, clinics, and commercial enterprises throughout:'
if old_ol in olwp:
    olwp = olwp.replace(old_ol, new_ol_wp)

with open(ol_wp, "w", encoding="utf-8") as f:
    f.write(olwp)

print("Updated office-location in HTML and WP")

# consultation
cs_html = os.path.join(html_base, "consultation", "index.html")
cs_wp = os.path.join(wp_base, "template-parts", "pages", "consultation.php")

with open(cs_html, "r", encoding="utf-8") as f:
    cs = f.read()

old_cs = 'identify clear search visibility opportunities, and provide straightforward recommendations tailored to your budget.'
new_cs = 'identify clear search visibility opportunities across our <a href="../services/index.html">Services Overview: Web Development &amp; SEO Packages</a>, and provide straightforward recommendations tailored to your budget.'
if old_cs in cs:
    cs = cs.replace(old_cs, new_cs)

with open(cs_html, "w", encoding="utf-8") as f:
    f.write(cs)

with open(cs_wp, "r", encoding="utf-8") as f:
    cswp = f.read()

new_cs_wp = 'identify clear search visibility opportunities across our <a href="<?php echo esc_url(home_url(\'/services/\')); ?>">Services Overview: Web Development &amp; SEO Packages</a>, and provide straightforward recommendations tailored to your budget.'
if old_cs in cswp:
    cswp = cswp.replace(old_cs, new_cs_wp)

with open(cs_wp, "w", encoding="utf-8") as f:
    f.write(cswp)

print("Updated consultation in HTML and WP")

# contact-us
cu_html = os.path.join(html_base, "contact-us", "index.html")
cu_wp = os.path.join(wp_base, "template-parts", "pages", "contact-us.php")

with open(cu_html, "r", encoding="utf-8") as f:
    cu = f.read()

old_cu = 'Whether you need a new website designed, an existing site audited, or local search visibility in Eastern Nepal'
new_cu = 'Whether you need a new website designed, an existing site audited, or local search visibility in Eastern Nepal through our <a href="../services/index.html">Services Overview: Web Development &amp; SEO Packages</a>'
if old_cu in cu:
    cu = cu.replace(old_cu, new_cu)

with open(cu_html, "w", encoding="utf-8") as f:
    f.write(cu)

with open(cu_wp, "r", encoding="utf-8") as f:
    cuwp = f.read()

new_cu_wp = 'Whether you need a new website designed, an existing site audited, or local search visibility in Eastern Nepal through our <a href="<?php echo esc_url(home_url(\'/services/\')); ?>">Services Overview: Web Development &amp; SEO Packages</a>'
if old_cu in cuwp:
    cuwp = cuwp.replace(old_cu, new_cu_wp)

with open(cu_wp, "w", encoding="utf-8") as f:
    f.write(cuwp)

print("Updated contact-us in HTML and WP")
