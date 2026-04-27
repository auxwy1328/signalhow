import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'
project = 'signalhow'
zone_id = '0ad6da50766a7e4b6792c0bedef0a48a'

# 1. Trigger deployment
url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/{project}/deployments'
body = json.dumps({}).encode()
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

# 2. Purge cache
url2 = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache'
body2 = json.dumps({"purge_everything": True}).encode()
req2 = urllib.request.Request(url2, data=body2, method='POST')
req2.add_header('Authorization', 'Bearer ' + token)
req2.add_header('Content-Type', 'application/json')
try:
    resp2 = urllib.request.urlopen(req2, timeout=15)
    data2 = json.loads(resp2.read())
    print('Cache purge - Success:', data2['success'])
except urllib.error.HTTPError as e:
    print(f'Cache purge - HTTP Error: {e.code}')
    print('Response:', e.read().decode()[:500])
