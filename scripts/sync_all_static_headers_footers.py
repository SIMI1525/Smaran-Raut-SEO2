import os
import glob
import re

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'

WHATSAPP_URL = "https://wa.me/9779714539838?text=Hi%2C%20I%27m%20interested%20in%20your%20website%20development%20and%20SEO%20services.%20I%27d%20like%20to%20discuss%20my%20requirements."
WHATSAPP_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.954 1.18-.175.201-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.176-.301-.019-.464.132-.614.136-.135.301-.351.452-.527.15-.176.201-.301.301-.501.1-.2.05-.376-.025-.527-.075-.15-.678-1.635-.929-2.241-.244-.59-.492-.51-.678-.52l-.578-.01c-.201 0-.527.075-.803.376s-1.054 1.03-1.054 2.51 1.079 2.91 1.229 3.111c.15.201 2.124 3.242 5.144 4.547.719.311 1.28.497 1.718.636.722.23 1.378.197 1.898.12.578-.087 1.78-.727 2.03-1.43.25-.704.25-1.309.175-1.43-.075-.121-.276-.197-.577-.348zM12.04 21.688c-1.75 0-3.468-.469-4.98-1.356l-.357-.208-3.708.973.99-3.613-.232-.37C2.793 15.42 2.22 13.56 2.22 11.64c0-5.414 4.406-9.82 9.82-9.82 2.623 0 5.089 1.021 6.944 2.877 1.856 1.856 2.878 4.321 2.878 6.943 0 5.415-4.406 9.822-9.822 9.822zM12.04 0C5.391 0 0 5.391 0 12.04c0 2.12.553 4.186 1.606 6.009L0 24l6.126-1.607c1.761.96 3.743 1.467 5.914 1.467 6.649 0 12.04-5.391 12.04-12.04C24.08 5.391 18.689 0 12.04 0z"/></svg>'
WHATSAPP_SVG_SM = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.954 1.18-.175.201-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.176-.301-.019-.464.132-.614.136-.135.301-.351.452-.527.15-.176.201-.301.301-.501.1-.2.05-.376-.025-.527-.075-.15-.678-1.635-.929-2.241-.244-.59-.492-.51-.678-.52l-.578-.01c-.201 0-.527.075-.803.376s-1.054 1.03-1.054 2.51 1.079 2.91 1.229 3.111c.15.201 2.124 3.242 5.144 4.547.719.311 1.28.497 1.718.636.722.23 1.378.197 1.898.12.578-.087 1.78-.727 2.03-1.43.25-.704.25-1.309.175-1.43-.075-.121-.276-.197-.577-.348zM12.04 21.688c-1.75 0-3.468-.469-4.98-1.356l-.357-.208-3.708.973.99-3.613-.232-.37C2.793 15.42 2.22 13.56 2.22 11.64c0-5.414 4.406-9.82 9.82-9.82 2.623 0 5.089 1.021 6.944 2.877 1.856 1.856 2.878 4.321 2.878 6.943 0 5.415-4.406 9.822-9.822 9.822zM12.04 0C5.391 0 0 5.391 0 12.04c0 2.12.553 4.186 1.606 6.009L0 24l6.126-1.607c1.761.96 3.743 1.467 5.914 1.467 6.649 0 12.04-5.391 12.04-12.04C24.08 5.391 18.689 0 12.04 0z"/></svg>'

old_h_cta = '<div class="header-cta-group">'
new_h_cta = f'''<div class="header-cta-group">
        <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" aria-label="Chat on WhatsApp">
          {WHATSAPP_SVG}
          <span class="btn-whatsapp-text">WhatsApp</span>
        </a>'''

old_drawer_cta_pattern = r'(<div style="margin-top: 2rem;">\s*<button class="btn btn-primary btn-consultation"[^>]*>.*?</button>\s*</div>)'
new_drawer_cta = f'''<div style="margin-top: 2rem; display: flex; flex-direction: column; gap: 0.75rem;">
      <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; justify-content: center;">
        {WHATSAPP_SVG}
        <span>Chat on WhatsApp</span>
      </a>
      <button class="btn btn-primary btn-consultation" style="width: 100%;" data-modal="consultation">
        Book Consultation
      </button>
    </div>'''

footer_target = 'Smaran Raut - No.1 SEO Expert in Itahari &rarr;</a>'
new_footer_addition = f'''Smaran Raut - No.1 SEO Expert in Itahari &rarr;</a>
          </p>
          <div style="margin-top: 1rem;">
            <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-size: 0.85rem; padding: 0.5rem 1rem;">
              {WHATSAPP_SVG_SM}
              <span>Chat on WhatsApp</span>
            </a>
          </div>'''

count = 0
for root, dirs, files in os.walk(STATIC_DIR):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified = False
            # Header CTA
            if 'aria-label="Chat on WhatsApp"' not in content and old_h_cta in content:
                content = content.replace(old_h_cta, new_h_cta, 1)
                modified = True
            
            # Mobile drawer CTA
            if '<span>Chat on WhatsApp</span>' not in content:
                m = re.search(old_drawer_cta_pattern, content)
                if m:
                    content = re.sub(old_drawer_cta_pattern, new_drawer_cta, content)
                    modified = True
            
            # Footer CTA
            if footer_target + '\n          </p>' in content and 'Chat on WhatsApp</span>\n            </a>\n          </div>' not in content:
                content = content.replace(footer_target + '\n          </p>', new_footer_addition)
                modified = True
            elif footer_target + '\r\n          </p>' in content and 'Chat on WhatsApp</span>\r\n            </a>\r\n          </div>' not in content:
                content = content.replace(footer_target + '\r\n          </p>', new_footer_addition)
                modified = True
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Updated header and footer WhatsApp CTAs in {count} HTML files!")
