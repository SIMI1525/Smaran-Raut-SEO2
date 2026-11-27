with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\data\site-data.js', encoding='utf-8') as f:
    c = f.read()

for line in c.splitlines():
    if 'smaran' in line or 'netlify' in line:
        print('site-data.js:', line)

with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\js\app.js', encoding='utf-8') as f:
    c = f.read()

for line in c.splitlines():
    if 'smaran' in line or 'netlify' in line:
        print('app.js:', line)
