import glob
import os

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)

with_dropdown = []
without_dropdown = []

for hf in sorted(html_files):
    if "verify.html" in hf or "googleae9e2a9d82bc15ed.html" in hf:
        continue
    rel = os.path.relpath(hf, site_dir).replace("\\", "/")
    c = open(hf, encoding="utf-8").read()
    if 'class="nav-dropdown"' in c:
        with_dropdown.append(rel)
    else:
        without_dropdown.append(rel)

print(f"Total HTML content files: {len(with_dropdown) + len(without_dropdown)}")
print(f"Files WITH nav-dropdown ({len(with_dropdown)}):")
for f in with_dropdown[:10]:
    print("  +", f)
if len(with_dropdown) > 10:
    print(f"  ... and {len(with_dropdown) - 10} more")

print(f"\nFiles WITHOUT nav-dropdown ({len(without_dropdown)}):")
for f in without_dropdown:
    print("  -", f)
