with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="knowledge-card"[^>]*>.*?</div>\s*</div>', text, re.DOTALL)
print("Knowledge cards found:", len(matches))
if matches:
    print("Sample card:\n", matches[0][:800])
