import os, glob, re

base_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
files = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)

patterns = [
    r'http://smaran',
    r'http://www\.smaran',
    r'https://www\.smaran',
    r'smaranraut\.com\.np',
    r'smaran-seo\.netlify\.app'
]

found = {}
for f in files:
    if ".git" in f or "scripts" in f or ".venv" in f: continue
    rel = os.path.relpath(f, base_dir)
    try:
        content = open(f, 'r', encoding='utf-8', errors='ignore').read()
        for p in patterns:
            m = re.findall(p, content, re.IGNORECASE)
            if m:
                if rel not in found: found[rel] = []
                found[rel].append((p, len(m)))
    except:
        pass

for rel, res in sorted(found.items()):
    print(f"[{rel}]: {res}")
