with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

main_idx = text.find('<main')
footer_idx = text.find('<footer')
print(text[main_idx:main_idx+1500])
