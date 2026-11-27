import glob
import re
import os

service_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\*\index.html")

for f in sorted(service_files):
    slug = os.path.basename(os.path.dirname(f))
    c = open(f, encoding="utf-8").read()
    print(f"=== {slug} ===")
    # find list items linking to blog
    items = re.findall(r'<li>\s*<a\s+[^>]*href=["\']([^"\']*blog/[^"\']*)["\'][^>]*>(.*?)</a>\s*&mdash;\s*(.*?)</li>', c)
    for href, anc, desc in items:
        print(f"  {href}  -->  [{re.sub(r'<[^>]+>', '', anc).strip()}]  |  Desc: {desc.strip()[:60]}")
    print()
