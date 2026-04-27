import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'

# List zones
url = 'https://api.cloudflare.com/client/v4/zones'
req = urllib.request.Request(url)
req.add_header('Authorization', 'Bearer ' + token)
resp = urllib.request.urlopen(req, timeout=15)
data = json.loads(resp.read())
for z in data['result']:
    print(f'Zone: {z["name"]} - ID: {z["id"]}')

print()

# List pages projects
url2 = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects'
req2 = urllib.request.Request(url2)
req2.add_header('Authorization', 'Bearer ' + token)
resp2 = urllib.request.urlopen(req2, timeout=15)
data2 = json.loads(resp2.read())
for p in data2['result']:
    print(f'Pages project: "{p["name"]}" - subdomain: {p["subdomain"]}')
