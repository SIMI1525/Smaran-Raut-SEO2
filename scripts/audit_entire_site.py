import glob
import os

all_html = glob.glob(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\**\*.html', recursive=True)
print(f"Total HTML files in project: {len(all_html)}")

missing_dropdown = []
has_dropdown = []

for h in all_html:
    # skip google verification or partial files if any
    if 'google' in os.path.basename(h):
        continue
    with open(h, encoding='utf-8') as f:
        c = f.read()
    rel = os.path.relpath(h, r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo')
    if 'nav-dropdown' in c:
        has_dropdown.append(rel)
    else:
        missing_dropdown.append(rel)

print(f"Pages WITH nav-dropdown: {len(has_dropdown)}")
print(f"Pages WITHOUT nav-dropdown: {len(missing_dropdown)}")
print("\nPages without nav-dropdown:")
for p in missing_dropdown:
    print(" -", p)
