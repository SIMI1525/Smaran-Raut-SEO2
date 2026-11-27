import re

c = open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\index.html', encoding='utf-8').read()

for i in range(1, 5):
    m = re.search(rf'PACKAGE {i}:[\s\S]*?(?=<div class="package-card"|</section>)', c)
    if m:
        print(f"=== PACKAGE {i} ===")
        # print first 500 chars
        print(m.group(0)[:400])
        print()
