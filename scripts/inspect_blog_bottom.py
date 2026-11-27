with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\social-media-and-online-advertising\index.html', encoding='utf-8') as f:
    c = f.read()

print("Modal backdrop present:", 'modal-backdrop' in c)
print("Consultation modal present:", 'id="consultation-modal"' in c or 'data-modal="consultation"' in c)
print("Footer present:", '<footer' in c)
print("Scripts in bottom:")
import re
print(re.findall(r'<script[\s\S]*?</script>', c[-3000:]))
