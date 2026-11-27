import os
import re

html_dir = r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"
wp_theme_dir = r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo"

# Check each WP file to verify only 1 H1 exists and it's valid
wp_files = [os.path.join(wp_theme_dir, r) for r in [
    r"template-parts\hero.php",
    r"template-parts\services\seo-optimized-web-development.php",
    r"template-parts\services\local-seo-itahari.php",
    r"template-parts\services\technical-seo-audit.php",
    r"template-parts\services\core-web-vitals-speed.php",
    r"template-parts\services\ecommerce-seo-nepal.php",
    r"template-parts\services\enterprise-link-building.php",
    r"template-parts\pages\about-us.php",
    r"template-parts\pages\contact-us.php",
    r"template-parts\pages\case-studies.php",
    r"template-parts\pages\consultation.php",
    r"template-parts\pages\office-location.php",
]]

error_count = 0
for f in wp_files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    h1s = re.findall(r'<h1[^>]*>[\s\S]*?</h1>', c)
    if len(h1s) != 1:
        print(f"WARNING: {f} has {len(h1s)} H1 tags!")
        error_count += 1
    else:
        clean = ' '.join(re.sub(r'<[^>]+>', '', h1s[0]).split())
        print(f"[VERIFIED] {os.path.basename(f)}: {clean}")

print(f"\nVerification finished. Errors: {error_count}")
