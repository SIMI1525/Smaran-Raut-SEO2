with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('</ul>', text.find('hero-service-list'))
print(text[idx:idx+800])
