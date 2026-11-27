import re

c = open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\index.html', encoding='utf-8').read()
links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', c)
for href, anc in links:
    anc_clean = re.sub(r'<[^>]+>', '', anc).strip()
    if not href.startswith("http") and not href.startswith("#") and not href.startswith("tel") and not href.startswith("mailto"):
        print(f"  {href}  -->  [{anc_clean}]")
