import re

for slug in ['website-setup-and-management', 'seo-services-explained', 'social-media-and-online-advertising']:
    path = f'C:/Users/BN/.gemini/antigravity/scratch/smaran-raut-seo/blog/{slug}/index.html'
    c = open(path, encoding='utf-8').read()
    print(f"=== {slug} ===")
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', c)
    print("H2s:", [re.sub(r'<[^>]+>', '', h).strip() for h in h2s])
    art = re.findall(r'<article[^>]*>([\s\S]*?)</article>', c)
    content_to_check = art[0] if art else c
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services[^"\']*)["\'][^>]*>(.*?)</a>', content_to_check)
    for h, a in links:
        print("  Link:", h, "-->", re.sub(r'<[^>]+>', '', a).strip())
    print()
