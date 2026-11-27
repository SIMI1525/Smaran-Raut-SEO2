with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\seo-optimized-web-development\index.html', encoding='utf-8') as f:
    c = f.read()

import re
header_match = re.search(r'<header[^>]*>[\s\S]*?</header>', c)
if header_match:
    print("Header in services/seo-optimized-web-development/index.html:")
    print(header_match.group(0))

drawer_match = re.search(r'class="mobile-nav-drawer"', c)
print("\nMobile drawer present:", bool(drawer_match))
