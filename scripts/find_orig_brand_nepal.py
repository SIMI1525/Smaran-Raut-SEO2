import os
import glob
import re

backup_dir = r"C:\Users\BN\.gemini\antigravity\scratch\backups_website_wide_20261118"
html_backup = os.path.join(backup_dir, "smaran-raut-seo")

print("Checking backup directory:", os.path.exists(html_backup))

backup_files = glob.glob(os.path.join(html_backup, "**", "*.html"), recursive=True)
print(f"Total backup HTML files: {len(backup_files)}")

orig_h1s = {}
for bf in backup_files:
    if "scripts" in bf or "verify" in bf or "google" in bf:
        continue
    rel = os.path.relpath(bf, html_backup)
    with open(bf, "r", encoding="utf-8") as f:
        c = f.read()
    m = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', c, re.IGNORECASE)
    if m:
        clean = ' '.join(re.sub(r'<[^>]+>', '', m[0]).split())
        orig_h1s[rel] = clean

print(f"\nFiles originally containing 'Smaran Raut' or 'Nepal' in H1:")
for rel, h1 in sorted(orig_h1s.items()):
    has_brand = "smaran raut" in h1.lower()
    has_nepal = "nepal" in h1.lower()
    if has_brand or has_nepal:
        print(f"[{rel}] (Brand={has_brand}, Nepal={has_nepal}) -> {h1}")
