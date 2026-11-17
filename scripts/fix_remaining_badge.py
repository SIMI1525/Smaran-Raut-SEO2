import os
import re

STATIC_DIR = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
WP_DIR = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

REMAINING_PATTERN = re.compile(
    r'\s*<div class="verified-stamp"[^>]*>.*?</div>\s*</div>',
    re.DOTALL
)

def fix_file(filepath):
    if not os.path.exists(filepath):
        return False
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content, n = REMAINING_PATTERN.subn("", content)
    if n > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def run():
    count = 0
    # Static
    index_path = os.path.join(STATIC_DIR, "index.html")
    if fix_file(index_path):
        count += 1
    for item in os.listdir(STATIC_DIR):
        if item.startswith("seo-expert-"):
            p = os.path.join(STATIC_DIR, item, "index.html")
            if fix_file(p):
                count += 1
    
    # WP
    hero_php = os.path.join(WP_DIR, "template-parts", "hero.php")
    if fix_file(hero_php):
        count += 1
    geo_dir = os.path.join(WP_DIR, "template-parts", "geo")
    if os.path.exists(geo_dir):
        for item in os.listdir(geo_dir):
            if item.endswith(".php"):
                if fix_file(os.path.join(geo_dir, item)):
                    count += 1
    
    # generator script
    gen_script = os.path.join(STATIC_DIR, "scripts", "generate-locations.ps1")
    if fix_file(gen_script):
        count += 1

    print(f"Fixed remaining badge snippet in {count} files.")

if __name__ == "__main__":
    run()
