with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\index.html', encoding='utf-8') as f:
    c = f.read()

for line in c.splitlines():
    if 'smaran-seo.netlify.app' in line:
        print(line)
