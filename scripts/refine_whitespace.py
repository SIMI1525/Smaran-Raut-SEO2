import os
import re

STATIC_DIR = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
WP_DIR = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

REPLACEMENTS = [
    # 1. Inner page hero-section inline padding (bottom was too large when followed by another padded section)
    (r'<section class="hero-section" style="padding:\s*3\.5rem 0;">', '<section class="hero-section" style="padding: 2.5rem 0 2rem;">'),
    # 2. Inner page page-content-section inline padding
    (r'<section class="page-content-section" style="padding:\s*3\.5rem 0;">', '<section class="page-content-section" style="padding: 2.5rem 0 2.75rem;">'),
    # 3. Calculator section container padding-top
    (r'<section class="container" style="padding-top:\s*3\.5rem;">', '<section class="container" style="padding-top: 2rem;">'),
    # 4. Section headers with excessive margin-bottom
    (r'margin:\s*0 auto 3\.5rem;', 'margin: 0 auto 2.25rem;'),
    # 5. Section headers margin-bottom: 3rem
    (r'<div style="text-align: center; margin-bottom:\s*3rem;">', '<div style="text-align: center; margin-bottom: 2rem;">'),
]

def refine_directory(base_dir, ext):
    updated = 0
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(ext):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                new_content = content
                for pat, rep in REPLACEMENTS:
                    new_content = re.sub(pat, rep, new_content)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    updated += 1
    return updated

if __name__ == "__main__":
    n_static = refine_directory(STATIC_DIR, ".html")
    n_wp = refine_directory(WP_DIR, ".php")
    print(f"Whitespace refined: {n_static} static HTML files, {n_wp} WordPress PHP files")
