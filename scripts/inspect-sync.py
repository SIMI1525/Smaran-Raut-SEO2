import os

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
with open(os.path.join(site_dir, "verify.py"), "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines[155:195], start=155):
    print(f"{i}: {l}", end="")
