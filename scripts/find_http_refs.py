import os, glob, re

base_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
files = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)

http_refs = []
for f in files:
    if ".git" in f or "scripts" in f or ".venv" in f: continue
    rel = os.path.relpath(f, base_dir)
    try:
        content = open(f, 'r', encoding='utf-8', errors='ignore').read()
        # find http:// URLs (exclude schema.org, w3.org, etc.)
        matches = re.findall(r'http://(?!www\.w3\.org|schema\.org)[^\s"\'<>]+', content)
        if matches:
            http_refs.append((rel, matches))
    except:
        pass

print(f"Total files with non-schema http://: {len(http_refs)}")
for rel, m in http_refs:
    print(f"[{rel}]: {m}")
