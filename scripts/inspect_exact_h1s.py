import os
import glob
import re

theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"
php_files = glob.glob(os.path.join(theme_dir, "**", "*.php"), recursive=True)

exact_h1s = {}

for pf in php_files:
    rel = os.path.relpath(pf, theme_dir)
    with open(pf, "r", encoding="utf-8") as f:
        c = f.read()
    matches = re.findall(r'<h1[^>]*>[\s\S]*?</h1>', c, re.IGNORECASE)
    if matches:
        exact_h1s[rel] = matches

for k, v in sorted(exact_h1s.items()):
    for tag in v:
        print(f"{k} :: {tag}")
