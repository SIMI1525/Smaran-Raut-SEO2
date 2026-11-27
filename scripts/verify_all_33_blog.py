import glob
import re
import os

blog_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html")

def clean(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&amp;', '&')
    return ' '.join(t.split())

count_with_supp = 0
for f in sorted(blog_files):
    slug = os.path.basename(os.path.dirname(f))
    c = open(f, encoding="utf-8").read()
    
    # Check for supplementary H2 or section
    h2s = list(re.finditer(r'<h2[^>]*>(.*?)</h2>', c))
    last_h2 = clean(h2s[-1].group(1)) if h2s else ""
    
    # find service link in the last section
    last_pos = h2s[-1].start() if h2s else 0
    last_section = c[last_pos:]
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services[^"\']*)["\'][^>]*>(.*?)</a>', last_section)
    
    # filter footer links
    filtered_links = [(href, clean(anc)) for href, anc in links if clean(anc) not in ["Services", "SEO Web Development", "Local SEO Itahari", "SEO for Existing Sites", "Maintenance & Speed", "Maintenance &amp; Speed"]]
    
    if filtered_links:
        count_with_supp += 1
        print(f"PASS: {slug} -> Last H2: '{last_h2}' | Link: {filtered_links[0][1]}")
    else:
        print(f"FAIL: {slug} -> Last H2: '{last_h2}' | NO SUPPLEMENTARY SERVICE LINK!")

print(f"\nTotal articles: {len(blog_files)}, Articles with verified supplementary link: {count_with_supp}")
