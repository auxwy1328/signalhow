import urllib.request, json

token = open(r'C:\Users\15645\Desktop\cfToken.txt').read().strip()
account = 'b8faf46813646ff3625ffdbac9403fe8'
project = 'encrypted-chat-seo'

# Get latest deployment
url = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/{project}/deployments?per_page=1'
req = urllib.request.Request(url)
req.add_header('Authorization', 'Bearer ' + token)
req.add_header('Content-Type', 'application/json')
try:
    resp = urllib.request.urlopen(req, timeout=15)
    data = json.loads(resp.read())
    if data['result']:
        d = data['result'][0]
        deploy_id = d['id']
        print(f'Latest deploy: {deploy_id} - {d["latest_stage"]["name"]}')

        # Retry it
        url2 = f'https://api.cloudflare.com/client/v4/accounts/{account}/pages/projects/{project}/deployments/{deploy_id}/retry'
        req2 = urllib.request.Request(url2, data=b'', method='POST')
        req2.add_header('Authorization', 'Bearer ' + token)
        req2.add_header('Content-Type', 'application/json')
        try:
            resp2 = urllib.request.urlopen(req2, timeout=30)
            data2 = json.loads(resp2.read())
            print(f'Retry - Success: {data2["success"]}')
            if data2.get('result'):
                print(f'New deploy: {data2["result"]["id"]}')
            if data2.get('errors'):
                print(f'Errors: {data2["errors"]}')
        except urllib.error.HTTPError as e:
            print(f'Retry - HTTP Error: {e.code}')
            print(f'Response: {e.read().decode()[:500]}')
    else:
        print('No deployments found')
except Exception as e:
    print(f'Error: {e}')
