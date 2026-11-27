import glob
import re

site_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
html_files = glob.glob(site_dir + "/**/*.html", recursive=True)

phones = set()
wa_links = set()
emails = set()

for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    for m in re.findall(r'(\+977[\s-]?[0-9]{10}|9714539838|98[0-9]{8})', content):
        phones.add(m)
    for m in re.findall(r'href=["\']([^"\']*(?:wa\.me|whatsapp)[^"\']*)["\']', content):
        wa_links.add(m)
    for m in re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content):
        emails.add(m)

print("Phone numbers:", phones)
print("WhatsApp links:", wa_links)
print("Emails:", emails)
