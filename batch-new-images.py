import urllib.request, urllib.parse, json, hashlib, time, os, subprocess, sys

# Get token
req = urllib.request.Request("http://127.0.0.1:18432/get_token")
token = urllib.request.urlopen(req).read().decode().strip()
if not token.startswith("Bearer"):
    token = "Bearer " + token

API = "https://autoglm-api.zhipuai.cn/agentdr/v1/assistant/skills/generate-image"
SECRET = "38d2391985e2369a5fb8227d8e6cd5e5"

prompts = {
    # encryption.md - 1 cover + 3 body
    "safety/encryption/cover": "digital encryption concept, glowing lock icon with binary code streams on dark blue background, modern cybersecurity theme, professional tech illustration, no text",
    "safety/encryption/body1": "abstract visualization of cryptographic key exchange between two devices, glowing data streams with green particles on dark background, network security concept, professional tech illustration, no text",
    "safety/encryption/body2": "forward secrecy concept illustration, keys rotating and dissolving like sand, blue and green glow effect on dark background, cryptography visualization, professional illustration, no text",
    "safety/encryption/body3": "sealed envelope with digital padlock, data packets being encrypted before transmission, privacy protection concept on dark blue tech background, professional illustration, no text",
    # backup.md - 1 cover + 3 body
    "guides/backup/cover": "smartphone with cloud backup arrow and shield icon, data protection concept on dark gradient background, blue and purple tones, modern tech illustration, no text",
    "guides/backup/body1": "Android phone showing backup settings screen with green checkmark, local storage concept with microSD card icon, dark tech background, professional illustration, no text",
    "guides/backup/body2": "iPhone connected to iCloud with encrypted data streams, Apple logo subtle, blue gradient tech background, data sync concept, professional illustration, no text",
    "guides/backup/body3": "data transfer animation between two phones, progress bar with shield icon, device migration concept on dark background, green and blue tones, professional illustration, no text",
    # group-chat.md - 1 cover + 3 body
    "guides/group-chat/cover": "multiple user avatars in encrypted group chat bubble, Signal blue theme, connection lines between participants, dark background, modern tech illustration, no text",
    "guides/group-chat/body1": "group settings interface concept with member list and admin badges, user management icons, dark theme with blue accents, professional illustration, no text",
    "guides/group-chat/body2": "voting interface concept with multiple choice options and vote counts, poll result visualization, dark theme with green and blue accents, professional illustration, no text",
    "guides/group-chat/body3": "group chat security concept, encryption shield protecting multiple chat bubbles, privacy lock icon, dark blue tech background, professional illustration, no text",
}

base_dir = r"C:\Projects\signal-how\static\images"
success = 0
fail = 0

for rel_path, prompt in prompts.items():
    out_dir = os.path.join(base_dir, os.path.dirname(rel_path))
    os.makedirs(out_dir, exist_ok=True)
    fname = os.path.basename(rel_path) + ".jpg"
    out_path = os.path.join(out_dir, fname)

    ts = str(int(time.time()))
    sign_raw = f"100003&{ts}&{SECRET}"
    sign = hashlib.md5(sign_raw.encode()).hexdigest()

    body = json.dumps({"text": prompt}).encode()
    req = urllib.request.Request(API, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", token)
    req.add_header("X-Auth-Appid", "100003")
    req.add_header("X-Auth-TimeStamp", ts)
    req.add_header("X-Auth-Sign", sign)

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        img_url = data["data"]["image_url"]
        urllib.request.urlretrieve(img_url, out_path)
        print(f"OK: {rel_path}")
        success += 1
    except Exception as e:
        print(f"FAIL: {rel_path} - {e}")
        fail += 1
    time.sleep(2)

print(f"\nDone: {success} success, {fail} fail")

# Crop watermarks
if success > 0:
    print("\nCropping watermarks (97% x 88%)...")
    from PIL import Image
    cropped = 0
    for rel_path in prompts:
        out_path = os.path.join(base_dir, rel_path + ".jpg")
        if os.path.exists(out_path):
            img = Image.open(out_path)
            w, h = img.size
            cropped_img = img.crop((0, 0, int(w * 0.97), int(h * 0.88)))
            cropped_img.save(out_path, "JPEG", quality=92)
            cropped += 1
    print(f"Cropped {cropped} images")
