with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', encoding='utf-8') as f:
    c = f.read()

idx = c.find('class="mobile-nav-drawer"')
end_idx = c.find('</main>', idx)
# Or find closing tag of mobile-nav-drawer
drawer_end = c.find('</div>', c.find('class="mobile-drawer-cta"', idx))
print("Drawer segment:")
print(c[idx-5:drawer_end+14])
print("\nFollowed by:")
print(c[drawer_end+14:drawer_end+300])
