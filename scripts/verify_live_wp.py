import urllib.request
import re

urls = [
    ('Homepage', 'http://smaran-raut.local/'),
    ('Article', 'http://smaran-raut.local/blog/top-seo-experts-in-nepal/'),
    ('About Us', 'http://smaran-raut.local/about-us/'),
    ('Contact Us', 'http://smaran-raut.local/contact-us/')
]

for label, url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            status = resp.status
            html = resp.read().decode('utf-8', errors='ignore')
            wa_count = html.count('wa.me/9779714539838')
            print(f'[{label}] {url} -> Status: {status} | WhatsApp CTAs: {wa_count}')
    except Exception as e:
        print(f'[{label}] {url} -> Error: {e}')
