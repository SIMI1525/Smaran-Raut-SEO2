import re

c = open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', encoding='utf-8').read()

h = re.search(r'<header[^>]*>[\s\S]*?</header>', c)
if h:
    print("=== Header in blog/index.html ===")
    print(h.group(0))

m = re.search(r'<div class="mobile-nav-drawer"[\s\S]*?</div>\s*</div>', c)
if m:
    print("\n=== Mobile Nav Drawer in blog/index.html ===")
    print(m.group(0))
else:
    # check for any mobile drawer
    m2 = re.search(r'<div[^>]*class="[^"]*mobile[^"]*"[\s\S]*?</div>', c)
    if m2:
        print("\n=== Some mobile div ===")
        print(m2.group(0)[:300])
