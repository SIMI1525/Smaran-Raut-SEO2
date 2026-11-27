with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\js\app.js', encoding='utf-8') as f:
    js = f.read()

import re
for term in ['dropdown', 'mobile-menu-toggle', 'mobile-nav-drawer', 'mobile-dropdown-toggle', 'nav-dropdown']:
    m = re.findall(term, js)
    print(f"Occurrences of '{term}': {len(m)}")

# Print where dropdown logic is defined in js/app.js
idx = js.find('dropdown')
if idx != -1:
    print("\nDropdown snippet in app.js:")
    print(js[idx-100:idx+1500])
