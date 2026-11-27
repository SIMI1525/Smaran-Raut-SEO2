with open(r'C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\functions.php', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('function smaran_seo_homepage_seo_meta()')
end_idx = content.find('add_action(\'wp_head\', \'smaran_seo_homepage_seo_meta\', 1);')
print(content[idx:end_idx+65])
