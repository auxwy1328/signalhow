import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'
project = 'encrypted-chat-seo'

# Use the correct API to create a new deployment from Git branch
url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/{project}/deployments'
body = json.dumps({
    "source": {
        "type": "github",
        "config": {
            "branch": "main",
            "productionBranch": "main"
        }
    }
}).encode()
req = urllib.request.Request(url, data=body, method='POST')
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')
try:
    resp = urllib.request.urlopen(req, timeout=30)
    data = json.loads(resp.read())
    print('Success:', data['success'])
    if data.get('result'):
        print('Deploy ID:', data['result']['id'])
    if data.get('errors'):
        print('Errors:', data['errors'])
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code}')
    print('Response:', e.read().decode()[:500])
