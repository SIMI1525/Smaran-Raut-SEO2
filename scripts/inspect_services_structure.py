import glob
import re
import os

service_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\*\index.html")
service_files.append(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\services\index.html")

for f in sorted(service_files):
    slug = os.path.basename(os.path.dirname(f)) if "services\\" in f and not f.endswith("services\\index.html") else "services-overview"
    c = open(f, encoding="utf-8").read()
    
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
    h1_text = re.sub(r'<[^>]+>', '', h1[0]).strip() if h1 else ""
    
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', c, re.DOTALL)
    h2_texts = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
    
    print(f"=== {slug} ===")
    print(f"H1: {h1_text}")
    print(f"H2 count: {len(h2_texts)}")
    for h in h2_texts[:4]:
        print(f"  H2: {h}")
    print()
