with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('article-card blog-article-item')
print(text[idx-50:idx+800])
