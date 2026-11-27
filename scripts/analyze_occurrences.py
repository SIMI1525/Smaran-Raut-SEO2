import os, glob, re

base_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
files = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)

occurrences = []

for f in files:
    if ".git" in f or "scripts" in f or ".venv" in f: continue
    rel = os.path.relpath(f, base_dir)
    try:
        content = open(f, 'r', encoding='utf-8', errors='ignore').read()
        for i, line in enumerate(content.splitlines(), 1):
            if 'smaran-seo.netlify.app' in line:
                occurrences.append((rel, i, line.strip()))
    except:
        pass

print(f"Total occurrences of smaran-seo.netlify.app: {len(occurrences)}")
by_file = {}
for rel, line_no, text in occurrences:
    by_file.setdefault(rel, []).append((line_no, text))

for rel, lines in sorted(by_file.items()):
    print(f"\n[{rel}] ({len(lines)} lines):")
    for line_no, text in lines:
        print(f"  L{line_no}: {text[:110]}")
