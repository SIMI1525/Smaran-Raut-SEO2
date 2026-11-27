import urllib.request
import urllib.error
import re
from html.parser import HTMLParser
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

candidates = [
    ("Krishna Bogati", "https://krishnabogati.com.np/"),
    ("Ujjwal Rupakheti", "https://www.ujjwalrupakheti.com.np/"),
    ("Sushant Karn", "https://sushantkarn.info.np/"),
    ("Suman Dhami", "https://sumandhami.com.np/"),
    ("Diwakar Bhatt", "https://diwakarbhatt.com.np/"),
    ("Rahul Ranjan", "https://www.rahulranjan.com.np/"),
    ("Dipak Paneru", "https://dipakpaneru.com/"),
    ("Prabesh Ghimire", "https://ghimireprabesh.com.np/"),
    ("Prabesh Ghimire Alt", "https://prabeshghimire.com/"),
    ("Keshab Joshi", "https://krjoshi.com.np/"),
    ("Suraj Giri", "https://seoexpertinnepal.com/"),
    ("Rambabu Thapa", "https://nepal.wordcamp.org/2025/speaker/rambabu-thapa/"),
    ("K.K. Bhatta", "https://www.queensdigitalagency.com/seo-expert-nepal/"),
    ("Pujan Bishwakarma", "https://www.pujanglobalseo.com/"),
    ("Bikesh Tamang", "https://bikeshtamang.com.np/"),
    ("Aman Mishra", "https://amanmishra.com.np/"),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

class SimpleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.links = []
        self.text_chunks = []
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag.lower() == 'title':
            self.in_title = True
        elif tag.lower() in ('script', 'style'):
            self.in_script = True
        elif tag.lower() == 'meta':
            name = attr_dict.get('name', '').lower()
            prop = attr_dict.get('property', '').lower()
            if name == 'description' or prop == 'og:description':
                if not self.meta_desc:
                    self.meta_desc = attr_dict.get('content', '')
        elif tag.lower() == 'a':
            href = attr_dict.get('href', '')
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag.lower() == 'title':
            self.in_title = False
        elif tag.lower() in ('script', 'style'):
            self.in_script = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif not self.in_script:
            txt = data.strip()
            if txt:
                self.text_chunks.append(txt)

results = {}

for name, url in candidates:
    print(f"Fetching: {name} ({url})...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
            raw = resp.read().decode('utf-8', errors='ignore')
            parser = SimpleParser()
            parser.feed(raw)
            
            title = parser.title.strip()
            desc = parser.meta_desc.strip()
            linkedin = [l for l in parser.links if 'linkedin.com' in l]
            gbp = [l for l in parser.links if 'maps.google' in l or 'g.page' in l or 'google.com/maps' in l]
            body_text = ' '.join(parser.text_chunks)[:1000]
            
            results[name] = {
                'url': url,
                'status': resp.status,
                'title': title,
                'desc': desc,
                'linkedin': list(set(linkedin)),
                'gbp': list(set(gbp)),
                'text_sample': body_text[:400]
            }
            print(f"  OK: Title='{title[:60]}' | Desc='{desc[:80]}'")
    except Exception as e:
        print(f"  FAILED: {e}")
        results[name] = {'url': url, 'error': str(e)}

with open('candidate_research.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print("Finished. Saved to candidate_research.json")
