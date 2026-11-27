with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\seo-optimized-web-development\index.html', encoding='utf-8') as f:
    c = f.read()

idx = c.find('class="mobile-nav-drawer"')
end_idx = c.find('</main>', idx)
# find the closing div of mobile-nav-drawer
drawer_close = c.find('</div>\n\n  <main', idx)
if drawer_close == -1:
    drawer_close = c.find('</div>\n  <main', idx)
if drawer_close == -1:
    drawer_close = c.find('<main', idx)

print("Mobile drawer from services/seo-optimized-web-development:")
print(c[idx-5:drawer_close])
