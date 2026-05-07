import os, re, subprocess, sys, time, urllib.request
from PIL import Image

script_dir = r'C:\Users\15645\.openclaw-autoclaw\skills\autoglm-generate-image'
script_path = os.path.join(script_dir, 'generate-image.py')
project_dir = r'C:\Projects\signal-how'

images = [
    ("guides/signal-verification", [
        ("cover.jpg", "Smartphone screen showing Signal app verification code input field with SMS message notification, blue Signal color scheme, security lock icon, clean modern design, 16:9 ratio", "cover"),
        ("phone-format.jpg", "Mobile phone number input screen showing correct +86 international format for Chinese phone number registration, with green checkmark indicator and red cross for wrong formats", "body1"),
        ("voice-verify.jpg", "Signal app voice verification screen showing Call Me button and incoming phone call with 6-digit code being spoken, step by step illustration", "body2"),
        ("intercept-settings.jpg", "Smartphone settings screen showing SMS blocking and spam filter options with toggle switches, multiple Chinese phone brand interfaces", "body3"),
    ]),
]

success = 0
for slug, imgs in images:
    for filename, prompt, img_type in imgs:
        out_dir = os.path.join(project_dir, "static", "images", slug.replace('/', os.sep))
        out_path = os.path.join(out_dir, filename)
        print(f"[{slug}/{filename}]...", end=" ", flush=True)
        try:
            result = subprocess.run([sys.executable, script_path, prompt], capture_output=True, text=True, timeout=60, cwd=script_dir)
            output = result.stdout + result.stderr
            url_match = re.search(r'(https://[^\s"\']+\.(jpg|png|jpeg|webp))', output)
            if not url_match:
                print("FAIL (no URL)"); continue
            os.makedirs(out_dir, exist_ok=True)
            tmp_path = out_path + '.tmp'
            urllib.request.urlretrieve(url_match.group(1), tmp_path)
            img = Image.open(tmp_path)
            w, h = img.size
            if img_type == "cover":
                img.crop((0, 0, w, int(h*0.88))).save(out_path, 'JPEG', quality=92)
            else:
                img.crop((0, 0, int(w*0.97), int(h*0.88))).save(out_path, 'JPEG', quality=92)
            os.remove(tmp_path)
            print(f"OK ({os.path.getsize(out_path)//1024}KB)")
            success += 1
        except Exception as e:
            print(f"FAIL ({e})")
        time.sleep(0.5)

print(f"\nImages: {success}/4")
