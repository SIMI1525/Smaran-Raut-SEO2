import os
import glob
import re

base_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"

files = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)

domain_refs = {}

for f in files:
    if ".git" in f or "scripts" in f or ".venv" in f:
        continue
    rel = os.path.relpath(f, base_dir)
    try:
        with open(f, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
        
        matches = re.findall(r'https?://[a-zA-Z0-9.-]*(?:smaran|netlify)[a-zA-Z0-9.-]*[^\s"\'<>]*', content)
        if matches:
            domain_refs[rel] = set(matches)
    except:
        pass

print(f"Total files with domain references: {len(domain_refs)}")
for rel, urls in sorted(domain_refs.items()):
    print(f"\n[{rel}] ({len(urls)} distinct domain URLs):")
    for u in sorted(urls)[:10]:
        print(f"  {u}")
