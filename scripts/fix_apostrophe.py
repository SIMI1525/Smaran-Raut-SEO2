with open(r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\what-is-seo.php", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(r"A Beginner\'s Guide", "A Beginner's Guide")
with open(r"C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\blog\what-is-seo.php", "w", encoding="utf-8") as f:
    f.write(c)

with open(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\what-is-seo\index.html", "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace(r"A Beginner\'s Guide", "A Beginner's Guide")
with open(r"C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\what-is-seo\index.html", "w", encoding="utf-8") as f:
    f.write(c2)

print("Fixed apostrophe in what-is-seo files successfully!")
