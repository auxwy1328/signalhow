import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'

for project in ['signalhow', 'encrypted-chat-seo']:
    url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/{project}/deployments?per_page=1'
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Bearer ' + token)
    req.add_header('Content-Type', 'application/json')
    resp = urllib.request.urlopen(req, timeout=15)
    data = json.loads(resp.read())
    if data['result']:
        d = data['result'][0]
        source = d.get('source', {})
        print(f'{project}: deploy={d["id"]} stage={d["latest_stage"]["name"]} source_type={source.get("type","?")}')
    else:
        print(f'{project}: no deployments')
