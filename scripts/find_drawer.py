with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', encoding='utf-8') as f:
    c = f.read()

idx = c.find('class="mobile-nav-drawer"')
print("Found at:", idx)
if idx != -1:
    print(c[idx-5:idx+2500])
else:
    # search for mobile in general
    import re
    matches = [m.start() for m in re.finditer(r'mobile', c)]
    print("Mobile matches:", len(matches))
    for m in matches[:5]:
        print(c[m-10:m+50])
