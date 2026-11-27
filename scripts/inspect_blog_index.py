with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('blog-grid')
if idx != -1:
    print(text[idx:idx+1500])
else:
    print("blog-grid not found, showing lines around article cards:")
    import re
    matches = re.findall(r'<article[^>]*>.*?</article>', text, re.DOTALL)
    print(f"Total articles: {len(matches)}")
    if matches:
        print(matches[0][:500])
