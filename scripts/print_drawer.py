with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', encoding='utf-8') as f:
    c = f.read()

idx = c.find('class="mobile-nav-drawer"')
print(c[idx+1500:idx+3200])
