import re

for slug in ['how-seo-works', 'what-is-seo']:
    c = open(f'C:/Users/BN/.gemini/antigravity/scratch/smaran-raut-seo/blog/{slug}/index.html', encoding='utf-8').read()
    print('===', slug, '===')
    s_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services[^"\']*)["\'][^>]*>(.*?)</a>', c)
    print('Service links count:', len(s_links))
    for href, anc in s_links:
        print('  ', href, '-->', re.sub(r'<[^>]+>', '', anc).strip())
    # find all H2s
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', c)
    print('H2s:', [re.sub(r'<[^>]+>', '', h).strip() for h in h2s])
