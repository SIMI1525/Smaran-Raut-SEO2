import os
import glob
import re

html_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

# Collect all HTML H1s
html_files = glob.glob(os.path.join(html_dir, "**", "*.html"), recursive=True)
html_h1s = {}

for hf in html_files:
    if "scripts" in hf or "verify" in hf or "google" in hf:
        continue
    rel = os.path.relpath(hf, html_dir)
    with open(hf, "r", encoding="utf-8") as f:
        c = f.read()
    m = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', c, re.IGNORECASE)
    if m:
        clean = [' '.join(re.sub(r'<[^>]+>', '', x).split()) for x in m]
        html_h1s[rel] = clean

# Collect all WP PHP H1s
php_files = glob.glob(os.path.join(theme_dir, "**", "*.php"), recursive=True)
php_h1s = {}

for pf in php_files:
    rel = os.path.relpath(pf, theme_dir)
    with open(pf, "r", encoding="utf-8") as f:
        c = f.read()
    m = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', c, re.IGNORECASE)
    if m:
        clean = [' '.join(re.sub(r'<[^>]+>', '', x).split()) for x in m]
        # Filter out empty like <?php the_title(); ?> where strip tag gives empty
        filtered = [x for x in clean if x and not x.startswith('<?php')]
        if filtered:
            php_h1s[rel] = filtered

print(f"Total HTML files with H1: {len(html_h1s)}")
print(f"Total WP template files with static H1: {len(php_h1s)}")

# Print all
print("\n--- ALL PAGES AND THEIR CURRENT H1 ---")
for k in sorted(html_h1s.keys()):
    print(f"{k} : {html_h1s[k]}")
