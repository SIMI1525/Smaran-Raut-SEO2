import os
import re

STATIC_DIR = r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo'
WP_DIR = r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo'

WHATSAPP_URL = "https://wa.me/9779714539838?text=Hi%2C%20I%27m%20interested%20in%20your%20website%20development%20and%20SEO%20services.%20I%27d%20like%20to%20discuss%20my%20requirements."

WHATSAPP_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.954 1.18-.175.201-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.176-.301-.019-.464.132-.614.136-.135.301-.351.452-.527.15-.176.201-.301.301-.501.1-.2.05-.376-.025-.527-.075-.15-.678-1.635-.929-2.241-.244-.59-.492-.51-.678-.52l-.578-.01c-.201 0-.527.075-.803.376s-1.054 1.03-1.054 2.51 1.079 2.91 1.229 3.111c.15.201 2.124 3.242 5.144 4.547.719.311 1.28.497 1.718.636.722.23 1.378.197 1.898.12.578-.087 1.78-.727 2.03-1.43.25-.704.25-1.309.175-1.43-.075-.121-.276-.197-.577-.348zM12.04 21.688c-1.75 0-3.468-.469-4.98-1.356l-.357-.208-3.708.973.99-3.613-.232-.37C2.793 15.42 2.22 13.56 2.22 11.64c0-5.414 4.406-9.82 9.82-9.82 2.623 0 5.089 1.021 6.944 2.877 1.856 1.856 2.878 4.321 2.878 6.943 0 5.415-4.406 9.822-9.822 9.822zM12.04 0C5.391 0 0 5.391 0 12.04c0 2.12.553 4.186 1.606 6.009L0 24l6.126-1.607c1.761.96 3.743 1.467 5.914 1.467 6.649 0 12.04-5.391 12.04-12.04C24.08 5.391 18.689 0 12.04 0z"/></svg>'
WHATSAPP_SVG_SM = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.954 1.18-.175.201-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.176-.301-.019-.464.132-.614.136-.135.301-.351.452-.527.15-.176.201-.301.301-.501.1-.2.05-.376-.025-.527-.075-.15-.678-1.635-.929-2.241-.244-.59-.492-.51-.678-.52l-.578-.01c-.201 0-.527.075-.803.376s-1.054 1.03-1.054 2.51 1.079 2.91 1.229 3.111c.15.201 2.124 3.242 5.144 4.547.719.311 1.28.497 1.718.636.722.23 1.378.197 1.898.12.578-.087 1.78-.727 2.03-1.43.25-.704.25-1.309.175-1.43-.075-.121-.276-.197-.577-.348zM12.04 21.688c-1.75 0-3.468-.469-4.98-1.356l-.357-.208-3.708.973.99-3.613-.232-.37C2.793 15.42 2.22 13.56 2.22 11.64c0-5.414 4.406-9.82 9.82-9.82 2.623 0 5.089 1.021 6.944 2.877 1.856 1.856 2.878 4.321 2.878 6.943 0 5.415-4.406 9.822-9.822 9.822zM12.04 0C5.391 0 0 5.391 0 12.04c0 2.12.553 4.186 1.606 6.009L0 24l6.126-1.607c1.761.96 3.743 1.467 5.914 1.467 6.649 0 12.04-5.391 12.04-12.04C24.08 5.391 18.689 0 12.04 0z"/></svg>'

CSS_SNIPPET = """
/* WhatsApp CTA Button */
.btn-whatsapp {
  background-color: #25D366;
  color: #FFFFFF !important;
  font-weight: 600;
  border: 1px solid #20BA5A;
  border-radius: var(--radius-sm, 6px);
  padding: 0.6rem 1.15rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 2px 4px rgba(37, 211, 102, 0.2);
  line-height: 1.25;
}
.btn-whatsapp:hover,
.btn-whatsapp:focus-visible {
  background-color: #1EBE5D;
  color: #FFFFFF !important;
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(37, 211, 102, 0.35);
}
.btn-whatsapp svg {
  flex-shrink: 0;
  fill: currentColor;
}
@media (max-width: 640px) {
  .header-cta-group .btn-whatsapp-text {
    display: none;
  }
  .header-cta-group .btn-whatsapp {
    padding: 0.55rem;
  }
}
"""

def add_css_if_missing(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '.btn-whatsapp' not in content:
        content += "\n" + CSS_SNIPPET
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added CSS to {file_path}")

# Add CSS to both dirs
add_css_if_missing(os.path.join(STATIC_DIR, 'css', 'styles.css'))
add_css_if_missing(os.path.join(STATIC_DIR, 'css', 'components.css'))
add_css_if_missing(os.path.join(WP_DIR, 'css', 'styles.css'))
add_css_if_missing(os.path.join(WP_DIR, 'css', 'components.css'))
add_css_if_missing(os.path.join(WP_DIR, 'style.css'))

# 1. Update WordPress Theme files
# 1A. header.php
wp_header_file = os.path.join(WP_DIR, 'header.php')
with open(wp_header_file, 'r', encoding='utf-8') as f:
    h = f.read()

# Desktop header CTA
old_h_cta = '<div class="header-cta-group">'
new_h_cta = f'''<div class="header-cta-group">
        <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" aria-label="Chat on WhatsApp">
          {WHATSAPP_SVG}
          <span class="btn-whatsapp-text">WhatsApp</span>
        </a>'''

if 'aria-label="Chat on WhatsApp"' not in h:
    h = h.replace(old_h_cta, new_h_cta, 1)

# Mobile drawer CTA
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
if 'btn-whatsapp' not in h or h.count('btn-whatsapp') < 2:
    h = re.sub(old_drawer_cta_pattern, new_drawer_cta, h)

with open(wp_header_file, 'w', encoding='utf-8') as f:
    f.write(h)
print("Updated header.php")

# 1B. footer.php
wp_footer_file = os.path.join(WP_DIR, 'footer.php')
with open(wp_footer_file, 'r', encoding='utf-8') as f:
    ft = f.read()

footer_target = 'Smaran Raut - No.1 SEO Expert in Itahari &rarr;</a>'
new_footer_addition = f'''Smaran Raut - No.1 SEO Expert in Itahari &rarr;</a>
          </p>
          <div style="margin-top: 1rem;">
            <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-size: 0.85rem; padding: 0.5rem 1rem;">
              {WHATSAPP_SVG_SM}
              <span>Chat on WhatsApp</span>
            </a>
          </div>'''
if 'btn-whatsapp' not in ft:
    ft = ft.replace(footer_target + '\n          </p>', new_footer_addition)
    with open(wp_footer_file, 'w', encoding='utf-8') as f:
        f.write(ft)
    print("Updated footer.php")

# 1C. template-parts/hero.php
wp_hero_file = os.path.join(WP_DIR, 'template-parts', 'hero.php')
with open(wp_hero_file, 'r', encoding='utf-8') as f:
    hr = f.read()

hero_cta_target = r'(<div class="hero-cta-stack">.*?<button class="btn btn-primary btn-consultation"[^>]*>.*?</button>\s*</div>)'
new_hero_cta = f'''<div class="hero-cta-stack">
              <a href="<?php echo esc_url(home_url('/services/')); ?>" class="btn btn-secondary">
                Explore Services &rarr;
              </a>
              <button class="btn btn-primary btn-consultation" data-modal="consultation" id="book-consultation-btn">
                Book a Consultation
              </button>
              <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" id="hero-whatsapp-btn">
                {WHATSAPP_SVG}
                <span>Chat on WhatsApp</span>
              </a>
            </div>'''
if 'hero-whatsapp-btn' not in hr:
    hr = re.sub(hero_cta_target, new_hero_cta, hr, flags=re.DOTALL)
    with open(wp_hero_file, 'w', encoding='utf-8') as f:
        f.write(hr)
    print("Updated hero.php")

# 1D. template-parts/pages/about-us.php
wp_about_file = os.path.join(WP_DIR, 'template-parts', 'pages', 'about-us.php')
with open(wp_about_file, 'r', encoding='utf-8') as f:
    ab = f.read()

about_target = 'keep websites running fast.</p>\n            </div>\n          </div>'
if about_target not in ab:
    about_target = 'keep websites running fast.</p>\r\n            </div>\r\n          </div>'

about_whatsapp_box = f'''keep websites running fast.</p>
            </div>
          </div>

          <!-- WhatsApp Contact CTA -->
          <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: var(--radius-md); padding: 1.5rem 1.75rem; margin: 2rem 0; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
            <div>
              <h3 style="font-size: 1.15rem; color: #166534; margin-bottom: 0.25rem;">Have Questions About Your Website or SEO?</h3>
              <p style="font-size: 0.95rem; color: #15803D; margin: 0;">Connect directly on WhatsApp to discuss your project requirements or get practical advice.</p>
            </div>
            <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">
              {WHATSAPP_SVG}
              <span>Chat on WhatsApp</span>
            </a>
          </div>'''
if 'btn-whatsapp' not in ab:
    ab = ab.replace(about_target, about_whatsapp_box, 1)
    with open(wp_about_file, 'w', encoding='utf-8') as f:
        f.write(ab)
    print("Updated template-parts/pages/about-us.php")

# 1E. template-parts/pages/contact-us.php
wp_contact_file = os.path.join(WP_DIR, 'template-parts', 'pages', 'contact-us.php')
with open(wp_contact_file, 'r', encoding='utf-8') as f:
    ct = f.read()

contact_target = r'(<p style="margin-bottom: 0\.5rem;"><strong>WhatsApp:</strong>.*?\(Click to Chat\) &rarr;</a></p>\s*<p style="margin-bottom: 0;"><strong>Response Window:</strong> Within 24 business hours</p>)'
new_contact_box = f'''<p style="margin-bottom: 0.5rem;"><strong>Response Window:</strong> Within 24 business hours</p>
            <div style="margin-top: 1.25rem;">
              <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; justify-content: center;">
                {WHATSAPP_SVG}
                <span>Message on WhatsApp</span>
              </a>
            </div>'''
if 'btn-whatsapp' not in ct:
    ct = re.sub(contact_target, new_contact_box, ct, flags=re.DOTALL)
    with open(wp_contact_file, 'w', encoding='utf-8') as f:
        f.write(ct)
    print("Updated template-parts/pages/contact-us.php")

# 2. Update Static site files
# 2A. index.html
static_index_file = os.path.join(STATIC_DIR, 'index.html')
with open(static_index_file, 'r', encoding='utf-8') as f:
    si = f.read()

# Desktop header CTA
old_si_h = '<div class="header-cta-group">'
new_si_h = f'''<div class="header-cta-group">
        <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" aria-label="Chat on WhatsApp">
          {WHATSAPP_SVG}
          <span class="btn-whatsapp-text">WhatsApp</span>
        </a>'''
if 'aria-label="Chat on WhatsApp"' not in si:
    si = si.replace(old_si_h, new_si_h, 1)

# Mobile drawer CTA
old_si_drawer_pattern = r'(<div style="margin-top: 2rem;">\s*<button class="btn btn-primary btn-consultation"[^>]*>.*?</button>\s*</div>)'
new_si_drawer = f'''<div style="margin-top: 2rem; display: flex; flex-direction: column; gap: 0.75rem;">
      <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; justify-content: center;">
        {WHATSAPP_SVG}
        <span>Chat on WhatsApp</span>
      </a>
      <button class="btn btn-primary btn-consultation" style="width: 100%;" data-modal="consultation">
        Book Consultation
      </button>
    </div>'''
if si.count('btn-whatsapp') < 2:
    si = re.sub(old_si_drawer_pattern, new_si_drawer, si)

# Hero CTA stack in static index
old_si_hero_pattern = r'(<div class="hero-cta-stack">.*?<button class="btn btn-primary btn-consultation"[^>]*>.*?</button>\s*</div>)'
new_si_hero = f'''<div class="hero-cta-stack">
              <a href="services/index.html" class="btn btn-secondary">
                Explore Services &rarr;
              </a>
              <button class="btn btn-primary btn-consultation" data-modal="consultation" id="book-consultation-btn">
                Book a Consultation
              </button>
              <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" id="hero-whatsapp-btn">
                {WHATSAPP_SVG}
                <span>Chat on WhatsApp</span>
              </a>
            </div>'''
if 'hero-whatsapp-btn' not in si:
    si = re.sub(old_si_hero_pattern, new_si_hero, si, flags=re.DOTALL)

# Footer in static index
if 'btn-whatsapp' not in si or si.count('btn-whatsapp') < 4:
    si = si.replace(footer_target + '\n          </p>', new_footer_addition)

with open(static_index_file, 'w', encoding='utf-8') as f:
    f.write(si)
print("Updated static index.html")

# 2B. static about-us/index.html
static_about_file = os.path.join(STATIC_DIR, 'about-us', 'index.html')
with open(static_about_file, 'r', encoding='utf-8') as f:
    sab = f.read()

# Header CTA
if 'aria-label="Chat on WhatsApp"' not in sab:
    sab = sab.replace(old_si_h, new_si_h, 1)
if sab.count('btn-whatsapp') < 2:
    sab = re.sub(old_si_drawer_pattern, new_si_drawer, sab)

# Footer
if footer_target + '\n          </p>' in sab:
    sab = sab.replace(footer_target + '\n          </p>', new_footer_addition)

# About content
static_about_target = 'keep websites running fast.</p>\n            </div>\n          </div>'
if static_about_target not in sab:
    static_about_target = 'keep websites running fast.</p>\r\n            </div>\r\n          </div>'
if 'Have Questions About Your Website or SEO?' not in sab:
    sab = sab.replace(static_about_target, about_whatsapp_box, 1)

with open(static_about_file, 'w', encoding='utf-8') as f:
    f.write(sab)
print("Updated static about-us/index.html")

# 2C. static contact-us/index.html
static_contact_file = os.path.join(STATIC_DIR, 'contact-us', 'index.html')
with open(static_contact_file, 'r', encoding='utf-8') as f:
    sct = f.read()

# Header CTA
if 'aria-label="Chat on WhatsApp"' not in sct:
    sct = sct.replace(old_si_h, new_si_h, 1)
if sct.count('btn-whatsapp') < 2:
    sct = re.sub(old_si_drawer_pattern, new_si_drawer, sct)

# Footer
if footer_target + '\n          </p>' in sct:
    sct = sct.replace(footer_target + '\n          </p>', new_footer_addition)

# Contact box
if 'Message on WhatsApp' not in sct:
    sct = re.sub(contact_target, new_contact_box, sct, flags=re.DOTALL)

with open(static_contact_file, 'w', encoding='utf-8') as f:
    f.write(sct)
print("Updated static contact-us/index.html")

print("All WhatsApp CTAs successfully applied!")
