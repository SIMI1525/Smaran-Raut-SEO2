for path in [
    r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\google-business-profile-optimization-nepal\index.html',
    r'C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\blog\how-seo-works\index.html'
]:
    print("===", path)
    with open(path, encoding='utf-8') as f:
        c = f.read()
    for line in c.splitlines():
        if 'smaran-seo.netlify.app' in line:
            print(" ", line)
