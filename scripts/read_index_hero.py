with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('hero-content')
print(text[idx+400:idx+1500])
