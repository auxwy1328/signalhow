"""Insert images into the 3 new articles."""
import os

base = r"C:\Projects\signal-how\content"

articles = [
    {
        "path": os.path.join(base, "safety", "encryption.md"),
        "images": ["/images/safety/encryption/cover.jpg"],
        "inserts": [
            ("## Signal Protocol 是什么", "\n![Signal Protocol 加密协议概述](/images/safety/encryption/body1.jpg)\n"),
            ("## Signal 加密与其他应用的对比", "\n![Signal 加密与其他应用对比](/images/safety/encryption/body2.jpg)\n"),
            ("## Signal 加密的安全性评估", "\n![Signal 安全性评估](/images/safety/encryption/body3.jpg)\n"),
        ],
    },
    {
        "path": os.path.join(base, "guides", "backup.md"),
        "images": ["/images/guides/backup/cover.jpg"],
        "inserts": [
            ("## Android 本地备份", "\n![Android 备份设置界面](/images/guides/backup/body1.jpg)\n"),
            ("## iOS iCloud 备份", "\n![iOS iCloud 备份示意](/images/guides/backup/body2.jpg)\n"),
            ("## 备份与设备迁移的区别", "\n![备份与设备迁移对比](/images/guides/backup/body3.jpg)\n"),
        ],
    },
    {
        "path": os.path.join(base, "guides", "group-chat.md"),
        "images": ["/images/guides/group-chat/cover.jpg"],
        "inserts": [
            ("## 创建群组", "\n![创建 Signal 群组](/images/guides/group-chat/body1.jpg)\n"),
            ("## 群组链接分享", "\n![群组链接分享设置](/images/guides/group-chat/body2.jpg)\n"),
            ("## 群组管理最佳实践", "\n![群组管理最佳实践](/images/guides/group-chat/body3.jpg)\n"),
        ],
    },
]

for art in articles:
    raw = open(art["path"], "rb").read().decode("utf-8")

    # Update images front matter
    imgs_line = 'images: ["' + '", "'.join(art["images"]) + '"]'
    if "images:" in raw:
        raw = raw.split("images:")[0] + "images: " + imgs_line + "\n" + raw.split("images:")[1].split("\n", 1)[1]
    else:
        # Add after date line
        raw = raw.replace('date: 2026-04-26', 'date: 2026-04-26\n' + imgs_line, 1)

    # Insert body images - process from bottom to top to preserve positions
    for heading, img_md in reversed(art["inserts"]):
        idx = raw.find(heading)
        if idx >= 0:
            # Insert image right after the heading line
            end_of_line = raw.index("\n", idx)
            raw = raw[:end_of_line] + img_md + raw[end_of_line:]
        else:
            print(f"WARNING: heading not found: {heading}")

    open(art["path"], "w", encoding="utf-8").write(raw)
    print(f"OK: {art['path']}")

print("All done")
