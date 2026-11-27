with open(r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\template-parts\pages\contact-us.php', 'r', encoding='utf-8') as f:
    contact_php = f.read()

idx = contact_php.find('Direct Inquiries')
if idx != -1:
    print(contact_php[idx-100:idx+800])
else:
    print(contact_php[800:2000])
