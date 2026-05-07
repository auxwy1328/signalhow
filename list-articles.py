import os, re
for root, dirs, files in os.walk(r'C:\Projects\signal-how\content'):
    for f in files:
        if f.endswith('.md') and f != '_index.md':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                text = fh.read()
            title = re.search(r'title:\s*"([^"]+)"', text)
            sec = os.path.basename(root)
            slug = f.replace('.md','')
            t = title.group(1) if title else 'N/A'
            print(f'{sec} | {slug} | {t}')
