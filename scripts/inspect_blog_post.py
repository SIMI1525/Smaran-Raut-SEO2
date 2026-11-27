with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\social-media-and-online-advertising\index.html', encoding='utf-8') as f:
    c = f.read()

import re
scripts = re.findall(r'<script[^>]*src=[\'"][^\'"]*[\'"][^>]*>', c)
print("Scripts in social-media-and-online-advertising:", scripts)

header_match = re.search(r'<header[^>]*>[\s\S]*?</header>', c)
if header_match:
    print("\nHeader in social-media-and-online-advertising:")
    print(header_match.group(0))
else:
    print("\nNo header found!")

drawer_match = re.search(r'class="mobile-nav-drawer"', c)
print("\nMobile drawer present:", bool(drawer_match))
