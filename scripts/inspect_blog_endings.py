import glob
import re
import os

blog_files = glob.glob(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\*\index.html")

for f in blog_files[:4]:
    slug = os.path.basename(os.path.dirname(f))
    content = open(f, encoding="utf-8").read()
    print(f"=== {slug} ===")
    # Look for the last H2 or callout section
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content)
    print("H2 count:", len(h2s))
    if h2s:
        print("Last H2:", h2s[-1])
    # Look for links to services
    s_links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*services[^"\']*)["\'][^>]*>(.*?)</a>', content)
    print("Service links:", s_links)
    print()
