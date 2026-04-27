import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'

# Try to create a deployment (POST to trigger rebuild from latest commit)
url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/signal-how/deployments'
body = json.dumps({}).encode()
req = urllib.request.Request(url, data=body, method='POST')
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')
try:
    resp = urllib.request.urlopen(req, timeout=15)
    data = json.loads(resp.read())
    print('Success:', data['success'])
    if data.get('result'):
        print('Deploy ID:', data['result']['id'])
    print('Errors:', data.get('errors', []))
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code}')
    print('Response:', e.read().decode()[:500])
