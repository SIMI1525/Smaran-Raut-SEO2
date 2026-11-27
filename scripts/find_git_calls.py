import json

with open(r'C:\Users\BN\.gemini\antigravity\brain\549e7608-99e6-4503-8a3a-8488d44e74e0\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        calls = obj.get('tool_calls', [])
        for c in calls:
            if c.get('name') == 'run_command':
                cmd = c.get('args', {}).get('CommandLine', '')
                if 'push' in cmd or 'commit' in cmd:
                    print('Command:', cmd)
