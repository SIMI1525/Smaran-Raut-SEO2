import re

c = open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\index.html', encoding='utf-8').read()
lists = re.findall(r'<ul class="package-features-list">([\s\S]*?)</ul>', c)
for i, l in enumerate(lists):
    print(f"=== Package {i+1} Features ===")
    items = re.findall(r'<li>[\s\S]*?<span>(.*?)</span>', l)
    for it in items:
        print("  *", it)
    print()
