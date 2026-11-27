import json

with open(r'C:\Users\BN\.gemini\antigravity\brain\549e7608-99e6-4503-8a3a-8488d44e74e0\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            content = data.get('content', '')
            if 'Top SEO Experts in Nepal' in content:
                print("FOUND PROMPT:")
                print(content)
                break
