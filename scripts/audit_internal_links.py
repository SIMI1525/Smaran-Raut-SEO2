import os
import glob
import re
import json

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
blog_dirs = [d for d in glob.glob(os.path.join(site_dir, "blog", "*")) if os.path.isdir(d)]

print(f"Total blog directories: {len(blog_dirs)}")

article_data = {}

for bd in sorted(blog_dirs):
    slug = os.path.basename(bd)
    index_file = os.path.join(bd, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
        h1 = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip() if h1_m else "No H1"
        
        # Check direct answer box
        has_direct_answer = "direct-answer-box" in content
        
        # Find in-article links (links inside <article>)
        article_m = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
        in_article_links = []
        if article_m:
            raw_links = re.findall(r'<a\s+href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>', article_m.group(1), re.DOTALL)
            for href, txt in raw_links:
                clean_txt = re.sub(r'<[^>]+>', '', txt).strip()
                in_article_links.append({"href": href, "anchor": clean_txt})
        
        # Extract H2s inside article
        h2s = []
        if article_m:
            raw_h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', article_m.group(1), re.DOTALL)
            h2s = [re.sub(r'<[^>]+>', '', h).strip() for h in raw_h2s]
            
        article_data[slug] = {
            "h1": h1,
            "has_direct_answer": has_direct_answer,
            "h2_count": len(h2s),
            "h2s": h2s,
            "links": in_article_links
        }

with open(os.path.join(site_dir, "scripts", "blog_audit.json"), "w", encoding="utf-8") as f:
    json.dump(article_data, f, indent=2)

print("Saved blog audit to scripts/blog_audit.json")

# Print summary
missing_direct_answer = [s for s, d in article_data.items() if not d["has_direct_answer"]]
print(f"Articles missing direct answer box: {len(missing_direct_answer)}")
for s in missing_direct_answer:
    print(f"  - {s}")

# Check service linking
services_linked = 0
for s, d in article_data.items():
    s_links = [l for l in d["links"] if "services" in l["href"]]
    if s_links:
        services_linked += 1

print(f"Articles linking to services: {services_linked} / {len(article_data)}")
