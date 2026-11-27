import glob
import re
import os

service_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\*\index.html")
service_files.append(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\index.html")

for f in sorted(service_files):
    rel = os.path.relpath(f, r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo")
    c = open(f, encoding="utf-8").read()
    
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', c)
    h1_text = re.sub(r'<[^>]+>', '', h1[0]).strip() if h1 else ""
    
    # links to blog
    blog_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*blog/[^"\']*)["\'][^>]*>(.*?)</a>', c)
    # links to other services
    serv_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services/[^"\']*)["\'][^>]*>(.*?)</a>', c)
    
    print(f"=== {rel} ===")
    print(f"H1: {h1_text}")
    print(f"Blog links ({len(blog_links)}):")
    for href, anc in blog_links:
        print(f"   {href}  -->  {re.sub(r'<[^>]+>', '', anc).strip()}")
    print(f"Service links ({len(serv_links)}):")
    for href, anc in serv_links:
        anc_clean = re.sub(r'<[^>]+>', '', anc).strip()
        if anc_clean not in ["Services", "SEO Web Development", "Local SEO Itahari", "SEO for Existing Sites", "Maintenance & Speed", "Maintenance &amp; Speed"]:
            print(f"   {href}  -->  {anc_clean}")
    print()
