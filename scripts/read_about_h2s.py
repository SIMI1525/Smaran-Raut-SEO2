with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\about-us\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', text)
print("H2s in about-us/index.html:")
for h in h2s:
    print(" -", re.sub(r'<[^>]+>', '', h).strip())
