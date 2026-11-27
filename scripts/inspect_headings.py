import re

for slug in ['how-seo-works', 'what-is-seo']:
    path = f'C:/Users/BN/.gemini/antigravity/scratch/smaran-raut-seo/blog/{slug}/index.html'
    content = open(path, encoding='utf-8').read()
    print(f"=== {slug} ===")
    matches = re.findall(r'<h2[^>]*>(.*?)</h2>\s*(?:<p[^>]*>(.*?)</p>)?', content, re.DOTALL)
    for h2, p in matches:
        h2_clean = re.sub(r'<[^>]+>', '', h2).strip()
        p_clean = re.sub(r'<[^>]+>', '', p).strip() if p else 'NO DIRECT P'
        print(f"H2: {h2_clean}")
        print(f"  P: {p_clean[:120]}...")
        print()
