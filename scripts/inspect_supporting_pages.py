import os
import re

base_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
pages = ["about-us", "contact-us", "consultation", "case-studies", "office-location"]

for p in pages:
    path = os.path.join(base_dir, p, "index.html")
    c = open(path, encoding="utf-8").read()
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
    h1_clean = re.sub(r'<[^>]+>', '', h1[0]).strip() if h1 else ""
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', c, re.DOTALL)
    print(f"=== {p} ===")
    print(f"H1: {h1_clean}")
    print(f"H2s: {[re.sub(r'<[^>]+>', '', h).strip() for h in h2s]}")
    # find links to services
    s_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services/[^"\']*)["\'][^>]*>(.*?)</a>', c)
    filtered = [(href, re.sub(r'<[^>]+>', '', anc).strip()) for href, anc in s_links if re.sub(r'<[^>]+>', '', anc).strip() not in ["Services", "SEO Web Development", "Local SEO Itahari", "SEO for Existing Sites", "Maintenance & Speed", "Maintenance &amp; Speed"]]
    print(f"Service links ({len(filtered)}):")
    for href, anc in filtered:
        print(f"   {href}  -->  {anc}")
    print()
