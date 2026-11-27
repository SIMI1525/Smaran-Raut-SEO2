import os
import re

wp_theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"
html_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"

cities = [
    "belbari", "biratnagar", "birtamod", "damak", "dhankuta",
    "dharan", "duhabi", "gaighat", "ilam", "inaruwa",
    "itahari", "jhumka", "lahan", "rajbiraj", "ramdhuni",
    "rangeli", "urlabari"
]

# 1. Update WordPress theme files
wp_updates = {}

# Homepage hero
wp_updates[r"template-parts\hero.php"] = (
    r'<h1 class="hero-title">SEO Expert in Itahari, Nepal</h1>',
    r'<h1 class="hero-title">SEO Expert in Itahari, Nepal - Smaran Raut</h1>'
)

# 17 geo pages
for city in cities:
    city_cap = city.capitalize()
    rel = f"template-parts\\geo\\{city}.php"
    wp_updates[rel] = (
        f'<h1 class="hero-title">SEO Expert in {city_cap}, Nepal</h1>',
        f'<h1 class="hero-title">SEO Expert in {city_cap}, Nepal - Smaran Raut</h1>'
    )

# Services
wp_updates[r"template-parts\services\seo-optimized-web-development.php"] = (
    r'<h1 class="hero-title"[^>]*>SEO-Optimized <span class="highlight">Website Development</span></h1>',
    r'<h1 class="hero-title" style="max-width: 950px;">SEO-Optimized <span class="highlight">Website Development</span> in Nepal</h1>'
)

wp_updates[r"template-parts\services\ecommerce-seo-nepal.php"] = (
    r'<h1 class="hero-title"[^>]*>E-Commerce SEO &amp; <span class="highlight">Store Optimization</span></h1>',
    r'<h1 class="hero-title" style="max-width: 950px;">E-Commerce SEO &amp; <span class="highlight">Store Optimization</span> in Nepal</h1>'
)

wp_updates[r"template-parts\services\local-seo-itahari.php"] = (
    r'<h1 class="hero-title"[^>]*>Local SEO & <span class="highlight">Google Business Profile Optimization</span></h1>',
    r'<h1 class="hero-title" style="max-width: 950px;">Local SEO &amp; Google Business Profile Optimization in <span class="highlight">Itahari & Eastern Nepal</span></h1>'
)

# About page
wp_updates[r"template-parts\pages\about-us.php"] = (
    r'<h1 class="hero-title">About Smaran Raut</h1>',
    r'<h1 class="hero-title">About Smaran Raut: SEO &amp; Web Development in Nepal</h1>'
)

# Blog articles
wp_updates[r"template-parts\blog\how-seo-works.php"] = (
    r'<h1 class="hero-title">How Does SEO Work\? Understanding Search Rankings</h1>',
    r'<h1 class="hero-title">How Does SEO Work? Understanding Search Rankings in Nepal</h1>'
)

wp_updates[r"template-parts\blog\schema-markup-implementation-guide.php"] = (
    r'<h1 class="hero-title">Schema Markup \(JSON-LD\) Implementation Guide</h1>',
    r'<h1 class="hero-title">Schema Markup (JSON-LD) Implementation Guide in Nepal</h1>'
)

wp_updates[r"template-parts\blog\what-is-seo.php"] = (
    r'<h1 class="hero-title">What Is SEO\? A Beginner\'s Guide to Search Optimization</h1>',
    r'<h1 class="hero-title">What Is SEO? A Beginner\'s Guide for Nepal Businesses</h1>'
)

print(f"Total WP templates to update: {len(wp_updates)}")

wp_ok = 0
for rel, (pattern, repl) in wp_updates.items():
    fp = os.path.join(wp_theme_dir, rel)
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    new_c, count = re.subn(pattern, repl, c, count=1)
    if count > 0:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_c)
        wp_ok += 1
        print(f"[WP RESTORED] {rel}")
    else:
        print(f"[WP FAIL MATCH] {rel}")

print(f"\nWP Restorations: {wp_ok}/{len(wp_updates)}")

# 2. Update HTML files
html_updates = {}

html_updates["index.html"] = (
    r'<h1 class="hero-title">SEO Expert in Itahari, Nepal</h1>',
    r'<h1 class="hero-title">SEO Expert in Itahari, Nepal - Smaran Raut</h1>'
)

for city in cities:
    city_cap = city.capitalize()
    rel = f"seo-expert-{city}\\index.html"
    html_updates[rel] = (
        f'<h1 class="hero-title">SEO Expert in {city_cap}, Nepal</h1>',
        f'<h1 class="hero-title">SEO Expert in {city_cap}, Nepal - Smaran Raut</h1>'
    )

html_updates[r"services\seo-optimized-web-development\index.html"] = (
    r'<h1 class="hero-title"[^>]*>SEO-Optimized <span class="highlight">Website Development</span></h1>',
    r'<h1 class="hero-title" style="max-width: 950px;">SEO-Optimized <span class="highlight">Website Development</span> in Nepal</h1>'
)

html_updates[r"services\ecommerce-seo-nepal\index.html"] = (
    r'<h1 class="hero-title"[^>]*>E-Commerce SEO &amp; <span class="highlight">Store Optimization</span></h1>',
    r'<h1 class="hero-title" style="max-width: 950px;">E-Commerce SEO &amp; <span class="highlight">Store Optimization</span> in Nepal</h1>'
)

html_updates[r"services\local-seo-itahari\index.html"] = (
    r'<h1 class="hero-title"[^>]*>Local SEO & <span class="highlight">Google Business Profile Optimization</span></h1>',
    r'<h1 class="hero-title" style="max-width: 950px;">Local SEO &amp; Google Business Profile Optimization in <span class="highlight">Itahari & Eastern Nepal</span></h1>'
)

html_updates[r"about-us\index.html"] = (
    r'<h1 class="hero-title">About Smaran Raut</h1>',
    r'<h1 class="hero-title">About Smaran Raut: SEO &amp; Web Development in Nepal</h1>'
)

html_updates[r"blog\how-seo-works\index.html"] = (
    r'<h1 class="hero-title">How Does SEO Work\? Understanding Search Rankings</h1>',
    r'<h1 class="hero-title">How Does SEO Work? Understanding Search Rankings in Nepal</h1>'
)

html_updates[r"blog\schema-markup-implementation-guide\index.html"] = (
    r'<h1 class="hero-title">Schema Markup \(JSON-LD\) Implementation Guide</h1>',
    r'<h1 class="hero-title">Schema Markup (JSON-LD) Implementation Guide in Nepal</h1>'
)

html_updates[r"blog\what-is-seo\index.html"] = (
    r'<h1 class="hero-title">What Is SEO\? A Beginner\'s Guide to Search Optimization</h1>',
    r'<h1 class="hero-title">What Is SEO? A Beginner\'s Guide for Nepal Businesses</h1>'
)

html_ok = 0
for rel, (pattern, repl) in html_updates.items():
    fp = os.path.join(html_dir, rel)
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    new_c, count = re.subn(pattern, repl, c, count=1)
    if count > 0:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_c)
        html_ok += 1
        print(f"[HTML RESTORED] {rel}")
    else:
        print(f"[HTML FAIL MATCH] {rel}")

print(f"\nHTML Restorations: {html_ok}/{len(html_updates)}")
