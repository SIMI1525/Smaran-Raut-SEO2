import os
import re

wp_theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

check_files = [
    ("Homepage", r"template-parts\hero.php"),
    ("SEO Web Development", r"template-parts\services\seo-optimized-web-development.php"),
    ("E-Commerce SEO", r"template-parts\services\ecommerce-seo-nepal.php"),
    ("Local SEO Itahari", r"template-parts\services\local-seo-itahari.php"),
    ("About Us", r"template-parts\pages\about-us.php"),
    ("How SEO Works", r"template-parts\blog\how-seo-works.php"),
    ("Schema Markup Guide", r"template-parts\blog\schema-markup-implementation-guide.php"),
    ("What Is SEO", r"template-parts\blog\what-is-seo.php"),
]

cities = [
    "belbari", "biratnagar", "birtamod", "damak", "dhankuta",
    "dharan", "duhabi", "gaighat", "ilam", "inaruwa",
    "itahari", "jhumka", "lahan", "rajbiraj", "ramdhuni",
    "rangeli", "urlabari"
]

for city in cities:
    check_files.append((f"SEO Expert {city.capitalize()}", f"template-parts\\geo\\{city}.php"))

for name, rel in check_files:
    fp = os.path.join(wp_theme_dir, rel)
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    m = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', c)
    if m:
        clean = ' '.join(re.sub(r'<[^>]+>', '', m[0]).split())
        print(f"[{name}] -> {clean}")
