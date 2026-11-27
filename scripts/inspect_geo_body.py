import re

c = open('C:/Users/BN/.gemini/antigravity/scratch/smaran-raut-seo/seo-expert-biratnagar/index.html', encoding='utf-8').read()
m = re.findall(r'<main[^>]*>([\s\S]*?)</main>', c)
if m:
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services[^"\']*)["\'][^>]*>(.*?)</a>', m[0])
    for href, anc in links:
        anc_clean = re.sub(r'<[^>]+>', '', anc).strip()
        print(href, '-->', anc_clean)
