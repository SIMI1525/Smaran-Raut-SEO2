import glob
import re
import os

blog_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html")

slug_to_h1 = {}
for f in sorted(blog_files):
    slug = os.path.basename(os.path.dirname(f))
    c = open(f, encoding="utf-8").read()
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
    if h1:
        h1_clean = re.sub(r'<[^>]+>', '', h1[0]).strip()
        slug_to_h1[slug] = h1_clean

import json
print(json.dumps(slug_to_h1, indent=2))
