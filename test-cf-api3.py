import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'

# List all projects to see exact names
url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects'
req = urllib.request.Request(url)
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')
try:
    resp = urllib.request.urlopen(req, timeout=15)
    data = json.loads(resp.read())
    print('Success:', data['success'])
    for p in data.get('result', []):
        print(f'  Project: "{p["name"]}" - subdomain: {p["subdomain"]}')
    if data.get('errors'):
        print('Errors:', data['errors'])
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code}')
    print('Response:', e.read().decode()[:500])
