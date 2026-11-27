with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\index.html', encoding='utf-8') as f:
    c1 = f.read()

with open(r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\social-media-and-online-advertising\index.html', encoding='utf-8') as f:
    c2 = f.read()

import re
head1 = re.search(r'<head>([\s\S]*?)</head>', c1).group(1)
head2 = re.search(r'<head>([\s\S]*?)</head>', c2).group(1)

# check style tags
styles1 = re.findall(r'<style>([\s\S]*?)</style>', head1)
styles2 = re.findall(r'<style>([\s\S]*?)</style>', head2)

print("Styles in blog/index.html:", len(styles1))
if styles1:
    print("Content of styles in blog/index.html:")
    for s in styles1:
        print(s[:500])

print("\nStyles in blog/social-media-and-online-advertising:", len(styles2))
if styles2:
    print("Content of styles in social-media-and-online-advertising:")
    for s in styles2:
        print(s[:500])
