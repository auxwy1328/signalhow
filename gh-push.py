#!/usr/bin/env python3
import os, json, base64, urllib.request, subprocess, sys
TOKEN = open(r'C:\Users\15645\Desktop\githubToken.txt','r').read().strip()
OWNER, REPO, BRANCH = "auxwy1328", "signalhow", "main"
BASE = r"C:\Projects\signal-how"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"
H = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json", "Content-Type": "application/json"}
def api(method, url, data=None):
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=H, method=method)
    try: return json.loads(urllib.request.urlopen(req, timeout=30).read())
    except urllib.error.HTTPError as e: return json.loads(e.read())
r = subprocess.run(["git", "diff", "--name-only", "HEAD~1"], capture_output=True, text=True, cwd=BASE)
changed = [f.strip() for f in r.stdout.strip().split('\n') if f.strip() and not f.strip().startswith('public/')]
print(f"Changed: {len(changed)} files (excluding public/)")
if not changed: sys.exit(0)
ref = api("GET", f"{API}/git/ref/heads/{BRANCH}")
remote_sha = ref["object"]["sha"]
tree = api("GET", f"{API}/git/trees/{remote_sha}?recursive=1")
entries = []
changed_set = set(changed)
for item in tree.get("tree", []):
    if item["type"] == "tree": entries.append({"path": item["path"], "mode": item["mode"], "type": "tree", "sha": item["sha"]})
    elif item["type"] == "blob" and item["path"] not in changed_set: entries.append({"path": item["path"], "mode": item["mode"], "type": "blob", "sha": item["sha"]})
for fpath in changed:
    full = os.path.join(BASE, fpath.replace("/", os.sep))
    if not os.path.exists(full): continue
    with open(full, "rb") as f: content = f.read()
    blob = api("POST", f"{API}/git/blobs", {"content": base64.b64encode(content).decode(), "encoding": "base64"})
    entries.append({"path": fpath, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    print(f"  BLOB {fpath}")
new_tree = api("POST", f"{API}/git/trees", {"base_tree": remote_sha, "tree": entries})
commit = api("POST", f"{API}/git/commits", {"message": "fix: add description/keywords to [params]", "tree": new_tree["sha"], "parents": [remote_sha]})
ref = api("PATCH", f"{API}/git/refs/heads/{BRANCH}", {"sha": commit["sha"]})
print("SUCCESS!" if "object" in ref else f"FAIL: {ref}")
