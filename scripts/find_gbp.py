import glob
import re

found = set()
for f in glob.glob(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\**\*.*', recursive=True):
    if '.git' in f or 'scripts' in f or '.venv' in f:
        continue
    try:
        c = open(f, encoding='utf-8', errors='ignore').read()
        m = re.findall(r'https?://(?:g\.page|maps\.google|www\.google\.com/maps)[^\s"\'<>]+', c)
        for u in m:
            found.add((os.path.basename(f), u))
    except Exception as e:
        pass

for fname, u in sorted(found):
    print(f"{fname} -> {u}")
