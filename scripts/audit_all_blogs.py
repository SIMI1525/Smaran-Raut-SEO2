import glob
import os

blog_files = glob.glob(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html')
print(f"Total blog articles found: {len(blog_files)}")

with_dropdown = 0
without_dropdown = 0

for bf in blog_files:
    with open(bf, encoding='utf-8') as f:
        c = f.read()
    if 'nav-dropdown' in c:
        with_dropdown += 1
    else:
        without_dropdown += 1

print(f"Blog articles with nav-dropdown: {with_dropdown}")
print(f"Blog articles WITHOUT nav-dropdown: {without_dropdown}")
