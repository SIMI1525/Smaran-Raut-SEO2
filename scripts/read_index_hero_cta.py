with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('</h1>')
print(text[idx:idx+1000])
