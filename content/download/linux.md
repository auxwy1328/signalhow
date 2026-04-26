---
title: "Signal Linux 下载"
description: "Signal Linux 版安装教程，覆盖 Debian/Ubuntu、Fedora、Arch Linux 等主流发行版的安装方法。"
date: 2026-04-05
slug: "linux"
tags: ["Signal", "Linux", "桌面版"]
category: "版本更新"
tagClass: "tag-update"
emoji: "🐧"
readTime: "3 分钟"
---

## Signal Linux 版安装

Signal 提供多种 Linux 发行版的安装包。

## Debian / Ubuntu

```bash
# 安装官方 GPG 密钥
curl -fsSL https://updates.signal.org/desktop/apt/keys.asc | sudo gpg --dearmor -o /usr/share/keyrings/signal-desktop-keyring.gpg

# 添加软件源
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/signal-desktop-keyring.gpg] https://updates.signal.org/desktop/apt xenial main" | sudo tee /etc/apt/sources.list.d/signal-xenial.list

# 安装
sudo apt update && sudo apt install signal-desktop
```

## Fedora

```bash
# 安装官方 GPG 密钥
curl -fsSL https://updates.signal.org/desktop/rpm/keys.asc | sudo gpg --dearmor -o /usr/share/keyrings/signal-desktop-keyring.gpg

# 添加软件源
echo "[signal-desktop]
baseurl=https://updates.signal.org/desktop/rpm/yum
enabled=1
gpgcheck=1
gpgkey=file:///usr/share/keyrings/signal-desktop-keyring.gpg" | sudo tee /etc/yum.repos.d/signal-desktop.repo

# 安装
sudo dnf install signal-desktop
```

## Arch Linux

Signal Desktop 在 Arch Linux 官方仓库中可用：

```bash
sudo pacman -S signal-desktop
```

## Flatpak（通用）

```bash
flatpak install flathub org.signal.Signal
```

## Snap（通用）

```bash
sudo snap install signal-desktop
```
