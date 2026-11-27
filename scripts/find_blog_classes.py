with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Classes with card:")
print(set(re.findall(r'class="([^"]*card[^"]*)"', text)))
print("H3 titles in blog/index.html:")
print(re.findall(r'<h3[^>]*>(.*?)</h3>', text)[:5])
