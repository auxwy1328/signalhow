import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'

# Test: list deployments
url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/signal-how/deployments?per_page=1'
req = urllib.request.Request(url)
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')
try:
    resp = urllib.request.urlopen(req, timeout=15)
    data = json.loads(resp.read())
    print('Success:', data['success'])
    if data['result']:
        d = data['result'][0]
        print('Latest deploy:', d['id'], '-', d['latest_stage']['name'])
    else:
        print('No deployments')
        print('Errors:', data.get('errors', []))
except Exception as e:
    print('Error:', e)
