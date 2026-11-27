with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\contact-us\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="contact-info')
if idx == -1:
    idx = text.find('wa.me')
print(text[idx-100:idx+600])
