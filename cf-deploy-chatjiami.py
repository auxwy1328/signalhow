import urllib.request, json, time

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'
project = 'encrypted-chat-seo'

# 1. Trigger deployment with manifest (branch name)
url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/{project}/deployments'
body = json.dumps({"branch": "main"}).encode()
req = urllib.request.Request(url, data=body, method='POST')
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')
try:
    resp = urllib.request.urlopen(req, timeout=30)
    data = json.loads(resp.read())
    print('Deploy trigger - Success:', data['success'])
    if data.get('result'):
        print('Deploy ID:', data['result']['id'])
    if data.get('errors'):
        print('Errors:', data['errors'])
except urllib.error.HTTPError as e:
    print(f'Deploy trigger - HTTP Error: {e.code}')
    print('Response:', e.read().decode()[:500])

# 2. IndexNow - find key file
import os, hashlib
key = ''
static_dir = r'C:\Projects\encrypted-chat-seo\static'
for f in os.listdir(static_dir):
    if f.endswith('.txt') and f not in ('robots.txt', 'BingSiteAuth.xml'):
        content = open(os.path.join(static_dir, f), 'r', encoding='utf-8').read().strip()
        if len(content) == 16 and all(c in '0123456789abcdef' for c in content):
            key = content
            print(f'IndexNow key found: {key} (file: {f})')
            break

if key:
    body2 = json.dumps({"host": "chatjiami.com", "key": key, "urlList": ["https://chatjiami.com/sitemap.xml"]}).encode()
    req2 = urllib.request.Request('https://api.indexnow.org/indexnow', data=body2, method='POST')
    req2.add_header('Content-Type', 'application/json; charset=utf-8')
    try:
        resp2 = urllib.request.urlopen(req2, timeout=15)
        print(f'IndexNow ping: {resp2.status}')
    except Exception as e:
        print(f'IndexNow error: {e}')
else:
    print('IndexNow: key file not found')
