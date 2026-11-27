import glob
import re
import os

blog_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html")

print(f"Total articles found: {len(blog_files)}")

for f in sorted(blog_files):
    slug = os.path.basename(os.path.dirname(f))
    c = open(f, encoding="utf-8").read()
    
    # Extract body or main content
    # Find all links to ../../services/
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services/[^"\']*)["\'][^>]*>(.*?)</a>', c)
    # filter out footer/nav links (nav links typically have "Services", "SEO Web Development", "Local SEO Itahari", etc.)
    body_links = []
    for href, anc in links:
        anc_clean = re.sub(r'<[^>]+>', '', anc).strip()
        if href.endswith("services/index.html") and anc_clean == "Services":
            continue
        if anc_clean in ["SEO Web Development", "Local SEO Itahari", "SEO for Existing Sites", "Maintenance & Speed", "Maintenance &amp; Speed"]:
            continue
        body_links.append((href, anc_clean))
        
    print(f"{slug}: {len(body_links)} body service links")
    for href, anc in body_links:
        print(f"   {href}  -->  [{anc}]")
