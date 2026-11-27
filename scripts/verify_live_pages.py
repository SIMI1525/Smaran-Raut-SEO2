import urllib.request
import re

urls = [
    "https://smaranraut.com.np/",
    "https://smaranraut.com.np/services/seo-optimized-web-development/",
    "https://smaranraut.com.np/seo-expert-itahari/",
    "https://smaranraut.com.np/blog/how-seo-works/",
    "https://smaranraut.com.np/about-us/",
    "https://smaranraut.com.np/contact-us/",
    "https://smaranraut.com.np/case-studies/",
    "https://smaranraut.com.np/privacy-policy/"
]

for u in urls:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode("utf-8")
    canon = re.findall(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', html)
    og_url = re.findall(r'<meta\s+property=["\']og:url["\']\s+content=["\']([^"\']+)["\']', html)
    jsonld_urls = re.findall(r'"url":\s*"([^"]+)"', html)
    print(f"URL: {u}")
    print(f"  Canonical: {canon[0] if canon else 'NONE'}")
    print(f"  OG URL:    {og_url[0] if og_url else 'NONE'}")
    print(f"  JSON-LD:   {jsonld_urls[:2]}")
