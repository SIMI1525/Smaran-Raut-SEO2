import os
import glob
import re

theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"
php_files = glob.glob(os.path.join(theme_dir, "**", "*.php"), recursive=True)

h1_data = []

for pf in php_files:
    with open(pf, "r", encoding="utf-8") as f:
        content = f.read()
    rel = os.path.relpath(pf, theme_dir)
    matches = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', content, re.IGNORECASE)
    if matches:
        for m in matches:
            # clean whitespace and tags
            clean_m = re.sub(r'<[^>]+>', '', m).strip()
            clean_m = ' '.join(clean_m.split())
            h1_data.append((rel, clean_m, m.strip()))

print(f"Total H1 matches in WordPress theme: {len(h1_data)}")
for rel, clean, raw in sorted(h1_data):
    print(f"[{rel}] -> {clean}")
