import glob
import os

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)

count = 0
for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        text = f.read()
    changed = False
    if '<span class="item-title">Top SEO Experts in Nepal</span>' in text:
        text = text.replace('<span class="item-title">Top SEO Experts in Nepal</span>', '<span class="item-title">SEO Experts in Nepal</span>')
        changed = True
    if '<strong>Top SEO Experts in Nepal</strong>' in text:
        text = text.replace('<strong>Top SEO Experts in Nepal</strong>', '<strong>SEO Experts in Nepal</strong>')
        changed = True
    if changed:
        with open(hf, "w", encoding="utf-8") as f:
            f.write(text)
        count += 1

print(f"Updated title in nav dropdown for {count} HTML files.")
