import urllib.request
import urllib.error
import re
from bs4 import BeautifulSoup
import ssl

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

for name, url in candidates:
    print(f"\n==========================================")
    print(f"Checking: {name} ({url})")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            status = resp.status
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
            meta_desc = ""
            desc_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
            if desc_tag:
                meta_desc = desc_tag.get('content', '').strip()
            
            # Find social / external links
            linkedin = [a['href'] for a in soup.find_all('a', href=True) if 'linkedin.com' in a['href']]
            maps = [a['href'] for a in soup.find_all('a', href=True) if 'google.com/maps' in a['href'] or 'g.page' in a['href']]
            
            # Extract main text snippet
            text = ' '.join(soup.stripped_strings)[:600]
            
            print(f"Status: {status}")
            print(f"Title: {title}")
            print(f"Meta Desc: {meta_desc}")
            print(f"LinkedIn: {linkedin[:2]}")
            print(f"Maps/GBP: {maps[:2]}")
            print(f"Text Snippet: {text[:300]}...")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
