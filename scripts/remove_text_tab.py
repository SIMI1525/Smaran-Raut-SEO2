import os
import re

STATIC_DIR = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
WP_DIR = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

BADGE_PATTERN = re.compile(
    r'\s*(?:<!--\s*(?:Authentic\s+)?Credential Badge.*?-->\s*)?<div class="floating-credential-badge">.*?</div>',
    re.DOTALL
)

def clean_file(filepath):
    if not os.path.exists(filepath):
        return False
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content, n = BADGE_PATTERN.subn("", content)
    if n > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def run():
    static_count = 0
    wp_count = 0

    # 1. Static site files
    index_path = os.path.join(STATIC_DIR, "index.html")
    if clean_file(index_path):
        static_count += 1
        print(f"Cleaned {index_path}")

    for item in os.listdir(STATIC_DIR):
        if item.startswith("seo-expert-"):
            page_path = os.path.join(STATIC_DIR, item, "index.html")
            if clean_file(page_path):
                static_count += 1
                print(f"Cleaned {page_path}")

    # 2. WordPress files
    hero_php = os.path.join(WP_DIR, "template-parts", "hero.php")
    if clean_file(hero_php):
        wp_count += 1
        print(f"Cleaned {hero_php}")

    geo_dir = os.path.join(WP_DIR, "template-parts", "geo")
    if os.path.exists(geo_dir):
        for item in os.listdir(geo_dir):
            if item.endswith(".php"):
                geo_path = os.path.join(geo_dir, item)
                if clean_file(geo_path):
                    wp_count += 1
                    print(f"Cleaned {geo_path}")

    # 3. Generator script
    gen_script = os.path.join(STATIC_DIR, "scripts", "generate-locations.ps1")
    if clean_file(gen_script):
        print(f"Cleaned {gen_script}")

    print(f"\nDone! Cleaned {static_count} static HTML files and {wp_count} WordPress PHP files.")

if __name__ == "__main__":
    run()
