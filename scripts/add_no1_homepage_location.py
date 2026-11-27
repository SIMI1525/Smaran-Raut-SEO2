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
wp_files = [r"template-parts\hero.php"] + [f"template-parts\\geo\\{city}.php" for city in cities]

wp_ok = 0
for rel in wp_files:
    fp = os.path.join(wp_theme_dir, rel)
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Target <h1 class="hero-title">SEO Expert in ...
    new_c = re.sub(
        r'<h1 class="hero-title">\s*SEO Expert in ([^<]+)</h1>',
        r'<h1 class="hero-title">No.1 SEO Expert in \1</h1>',
        c
    )
    if new_c != c:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_c)
        wp_ok += 1
        print(f"[WP OK] {rel}")
    else:
        print(f"[WP NO MATCH] {rel}")

print(f"WP files updated: {wp_ok}/{len(wp_files)}")

# 2. Update HTML files
html_files = ["index.html"] + [f"seo-expert-{city}\\index.html" for city in cities]

html_ok = 0
for rel in html_files:
    fp = os.path.join(html_dir, rel)
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    
    new_c = re.sub(
        r'<h1 class="hero-title">\s*SEO Expert in ([^<]+)</h1>',
        r'<h1 class="hero-title">No.1 SEO Expert in \1</h1>',
        c
    )
    if new_c != c:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_c)
        html_ok += 1
        print(f"[HTML OK] {rel}")
    else:
        print(f"[HTML NO MATCH] {rel}")

print(f"HTML files updated: {html_ok}/{len(html_files)}")
