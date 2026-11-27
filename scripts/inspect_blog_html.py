with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', encoding='utf-8') as f:
    c = f.read()

print("Length of blog/index.html:", len(c))
count_html = c.count('<html')
print("Count of <html:", count_html)
if count_html > 1:
    pos = 0
    while True:
        idx = c.find('<html', pos)
        if idx == -1: break
        print(f"<html found at {idx}")
        pos = idx + 1
