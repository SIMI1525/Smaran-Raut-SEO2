with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\top-seo-experts-in-nepal\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<table', text)]
if len(matches) > 1:
    print(text[matches[1]:matches[1]+2500])
