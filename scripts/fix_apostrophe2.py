with open(r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\what-is-seo.php", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(r"Beginner\'s", "Beginner's")
with open(r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\what-is-seo.php", "w", encoding="utf-8") as f:
    f.write(c)

with open(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\what-is-seo\index.html", "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace(r"Beginner\'s", "Beginner's")
with open(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\what-is-seo\index.html", "w", encoding="utf-8") as f:
    f.write(c2)

print("Apostrophe fixed cleanly!")
