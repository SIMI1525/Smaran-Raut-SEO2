import glob
import re
import os

blog_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html")

results = []
for f in sorted(blog_files):
    slug = os.path.basename(os.path.dirname(f))
    c = open(f, encoding="utf-8").read()
    
    # H1
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
    h1_text = re.sub(r'<[^>]+>', '', h1[0]).strip() if h1 else ""
    
    # Direct answer box
    has_direct_answer = ('direct-answer' in c or 'quick-answer' in c or 'key-takeaways' in c or 'article-lead' in c)
    
    # All H2s
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', c, re.DOTALL)
    h2_texts = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
    
    # In-body service links (excluding header/footer/nav)
    # Extract article content
    art = re.findall(r'<article[^>]*>([\s\S]*?)</article>', c)
    art_content = art[0] if art else c
    
    s_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services/[^"\']*)["\'][^>]*>(.*?)</a>', art_content)
    
    results.append({
        "slug": slug,
        "h1": h1_text,
        "has_direct_answer": has_direct_answer,
        "h2_count": len(h2_texts),
        "last_h2": h2_texts[-1] if h2_texts else "",
        "service_links_in_article": [(href, re.sub(r'<[^>]+>', '', anc).strip()) for href, anc in s_links]
    })

import json
print(json.dumps(results[:5], indent=2))
print("Total articles:", len(results))
missing_da = [r["slug"] for r in results if not r["has_direct_answer"]]
print("Missing direct answer:", missing_da)
no_service_link = [r["slug"] for r in results if not r["service_links_in_article"]]
print("No service link in article:", no_service_link)
