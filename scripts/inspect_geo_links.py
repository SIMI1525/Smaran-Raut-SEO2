import glob
import re
import os

geo_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\seo-expert-*\index.html")

print(f"Total geo landing pages: {len(geo_files)}")

for f in sorted(geo_files)[:3]:
    slug = os.path.basename(os.path.dirname(f))
    c = open(f, encoding="utf-8").read()
    
    # H1
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
    h1_text = re.sub(r'<[^>]+>', '', h1[0]).strip() if h1 else ""
    
    # In-body service links
    s_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services/[^"\']*)["\'][^>]*>(.*?)</a>', c)
    # In-body blog links
    b_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*blog/[^"\']*)["\'][^>]*>(.*?)</a>', c)
    
    print(f"=== {slug} ===")
    print(f"H1: {h1_text}")
    print("Service links in body:")
    for href, anc in s_links:
        anc_clean = re.sub(r'<[^>]+>', '', anc).strip()
        if anc_clean not in ["Services", "SEO Web Development", "Local SEO Itahari", "SEO for Existing Sites", "Maintenance & Speed", "Maintenance &amp; Speed"]:
            print(f"   {href}  -->  {anc_clean}")
    print("Blog links in body:")
    for href, anc in b_links:
        anc_clean = re.sub(r'<[^>]+>', '', anc).strip()
        print(f"   {href}  -->  {anc_clean}")
    print()
