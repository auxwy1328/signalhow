---
title: "Signal Linux 下载"
description: "Signal Linux桌面客户端完整安装教程，详细介绍在Debian、Ubuntu、Fedora、CentOS及Arch Linux等主流发行版上的安装方法，提供APT包管理器命令行安装、官方软件源配置、DNF和Pacman安装等多种方式，同时包含Snap包及直接安装包的替代安装方案。"
date: 2026-04-05
slug: "linux"
tags: ["Signal", "Linux", "桌面版"]
category: "版本更新"
tagClass: "tag-update"
emoji: "🐧"
readTime: "3 分钟"
images: ["/images/download/linux/cover.jpg"]
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
