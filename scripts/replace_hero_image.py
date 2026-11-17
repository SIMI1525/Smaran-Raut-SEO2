import os
import re

STATIC_DIR = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
WP_DIR = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

# Pattern to match <div class="photo-wrapper">...</div>
# including the inner SVG and any whitespace/comments
PHOTO_WRAPPER_PATTERN = re.compile(
    r'(<div class="photo-wrapper">)\s*(?:<!--.*?-->\s*)?<svg class="photo-svg-art".*?</svg>\s*(</div>)',
    re.DOTALL
)

def format_city(slug):
    # e.g. seo-expert-biratnagar -> Biratnagar
    parts = slug.replace("seo-expert-", "").split("-")
    return " ".join(p.capitalize() for p in parts)

def update_static_files():
    count = 0
    # 1. index.html
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        replacement = r'\1\n              <img src="images/hero-smaran-seo.jpg" alt="Smaran Raut - SEO Specialist &amp; Web Developer in Itahari" class="hero-photo-img" width="1024" height="636" fetchpriority="high">\n            \2'
        new_content, n = PHOTO_WRAPPER_PATTERN.subn(replacement, content, count=1)
        if n > 0:
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {index_path}")
            count += 1
        else:
            print(f"Warning: pattern not matched in {index_path}")

    # 2. 17 location directories
    for item in os.listdir(STATIC_DIR):
        if item.startswith("seo-expert-"):
            page_path = os.path.join(STATIC_DIR, item, "index.html")
            if os.path.exists(page_path):
                city = format_city(item)
                with open(page_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                replacement = rf'\1\n              <img src="../images/hero-smaran-seo.jpg" alt="Smaran Raut - SEO Specialist &amp; Web Developer in {city}" class="hero-photo-img" width="1024" height="636" fetchpriority="high">\n            \2'
                new_content, n = PHOTO_WRAPPER_PATTERN.subn(replacement, content, count=1)
                if n > 0:
                    with open(page_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {page_path} ({city})")
                    count += 1
                else:
                    print(f"Warning: pattern not matched in {page_path}")
    return count

def update_wp_files():
    count = 0
    # 1. template-parts/hero.php
    hero_path = os.path.join(WP_DIR, "template-parts", "hero.php")
    if os.path.exists(hero_path):
        with open(hero_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        img_tag = '<?php echo esc_url(get_template_directory_uri() . \'/images/hero-smaran-seo.jpg\'); ?>'
        replacement = rf'\1\n              <img src="{img_tag}" alt="Smaran Raut - SEO Specialist &amp; Web Developer in Itahari" class="hero-photo-img" width="1024" height="636" fetchpriority="high">\n            \2'
        new_content, n = PHOTO_WRAPPER_PATTERN.subn(replacement, content, count=1)
        if n > 0:
            with open(hero_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {hero_path}")
            count += 1
        else:
            print(f"Warning: pattern not matched in {hero_path}")

    # 2. template-parts/geo/*.php
    geo_dir = os.path.join(WP_DIR, "template-parts", "geo")
    if os.path.exists(geo_dir):
        for item in os.listdir(geo_dir):
            if item.endswith(".php"):
                slug = item[:-4]
                city = slug.capitalize()
                file_path = os.path.join(geo_dir, item)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                img_tag = '<?php echo esc_url(get_template_directory_uri() . \'/images/hero-smaran-seo.jpg\'); ?>'
                replacement = rf'\1\n              <img src="{img_tag}" alt="Smaran Raut - SEO Specialist &amp; Web Developer in {city}" class="hero-photo-img" width="1024" height="636" fetchpriority="high">\n            \2'
                new_content, n = PHOTO_WRAPPER_PATTERN.subn(replacement, content, count=1)
                if n > 0:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {file_path} ({city})")
                    count += 1
                else:
                    print(f"Warning: pattern not matched in {file_path}")
    return count

def update_generator_script():
    gen_path = os.path.join(STATIC_DIR, "scripts", "generate-locations.ps1")
    if os.path.exists(gen_path):
        with open(gen_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        replacement = r'<div class="photo-wrapper">\n              <img src="../images/hero-smaran-seo.jpg" alt="Smaran Raut - SEO Specialist &amp; Web Developer in $($loc.Name)" class="hero-photo-img" width="1024" height="636" fetchpriority="high">\n            </div>'
        # Pattern in generate-locations.ps1 has $($loc.Name) in some places or hardcoded
        # Let's see if PHOTO_WRAPPER_PATTERN matches
        new_content, n = PHOTO_WRAPPER_PATTERN.subn(r'\1\n              <img src="../images/hero-smaran-seo.jpg" alt="Smaran Raut - SEO Specialist &amp; Web Developer in $($loc.Name)" class="hero-photo-img" width="1024" height="636" fetchpriority="high">\n            \2', content, count=1)
        if n > 0:
            with open(gen_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {gen_path}")
        else:
            print(f"Notice: pattern not matched in {gen_path}, check manually")

if __name__ == "__main__":
    c_static = update_static_files()
    c_wp = update_wp_files()
    update_generator_script()
    print(f"\nDone! Static files updated: {c_static}, WordPress files updated: {c_wp}")
