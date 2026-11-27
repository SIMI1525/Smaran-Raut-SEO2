with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\about-us\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Core Service Offerings')
print(text[idx:idx+1500])
