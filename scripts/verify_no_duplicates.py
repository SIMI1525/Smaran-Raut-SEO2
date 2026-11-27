import urllib.request
import re

req = urllib.request.Request('http://smaran-raut.local/blog/top-seo-experts-in-nepal/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=5) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
    if head_match:
        for line in head_match.group(1).splitlines():
            line_str = line.strip()
            if any(k in line_str.lower() for k in ['<title', 'canonical', 'og:', 'twitter:', 'article:']):
                print(line_str)
