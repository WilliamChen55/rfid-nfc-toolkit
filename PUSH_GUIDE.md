# 推送指南（3 分钟把仓库发上 GitHub）

仓库已经建好，就在这个文件夹里。下面任选一种方式。

> 先把仓库里所有 `WilliamChen55` 替换成你的 GitHub 用户名。
> 在 PowerShell 里跑这一句即可全替换：
> ```powershell
> Get-ChildItem -Recurse -Include *.md,*.toml,*.yml,*.json,*.py | ForEach-Object { (Get-Content $_ -Raw) -replace 'WilliamChen55','你的用户名' | Set-Content $_ -NoNewline }
> ```

---

## 方式 A：命令行（推荐，最快）

### 1. 安装 Git（已有可跳过）

本机已经装了 Git：`C:\Program Files\Git\cmd\git.exe`

### 2. 在 GitHub 网页上先建空仓库

https://github.com/new
- Repository name: `rfid-nfc-toolkit`
- Public
- **不要**勾选 "Add a README file"

### 3. 推送

```powershell
cd "C:\Users\HP\Doubao\chats\2026-11-25\new-chat\rfid-nfc-toolkit"
git init -b main
git add -A
git commit -m "feat: initial release of rfid-nfc-toolkit"
git remote add origin https://github.com/你的用户名/rfid-nfc-toolkit.git
git push -u origin main
```

首次 push 会弹浏览器登录 GitHub，跟着走完即可（不需要手动生成 token）。

---

## 方式 B：网页上传（不想装命令行）

1. 打开发方式 A 第 2 步建好的空仓库
2. 点 **uploading an existing file**
3. 把 `rfid-nfc-toolkit` 文件夹里**所有文件和子文件夹**拖进去
4. Commit message 填 `feat: initial release`
5. Commit

> 注意：`.github` 和 `docs/_config.yml` 这两个以点/下划线开头的名字，网页上传也能识别，别漏放。

---

## 推完必做的 5 件事（决定能不能被搜到）

1. 仓库右上 **Settings → General**：
   - Description 填：`Cross-platform Python toolkit for reading, identifying and analyzing RFID/NFC tags`
   - 勾 **Template repository** 不用
2. **About 右侧齿轮 → Topics**，逐个添加（一次一个，回车确认）：
   ```
   rfid  nfc  iso14443  iso15693  iclass  mifare  hardware  serial-port
   protocol-analyzer  security-research  sdr  python  pyserial  inventory
   ```
3. **Settings → Pages**：Source 选 `Deploy from a branch`，分支 `main`，目录 `/docs` → Save
   几分钟后文档站上线，地址形如 `https://你的用户名.github.io/rfid-nfc-toolkit/`
4. **Releases → Draft a new release**：Tag 填 `v0.1.0`，标题 `v0.1.0 — initial release`，正文复制 `CHANGELOG.md` 里那段，Publish
   （有 release 才会进关注者的通知流）
5. **Profile 主页**：仓库页点 **Pin**，让访客第一眼看到

---

## 之后 72 小时的引流动作

按 `marketing/` 文件夹里的文案依次发：

| 顺序 | 文件 | 发到哪 |
| --- | --- | --- |
| 1 | `marketing/awesome-list-pr.md` | 给 awesome-* 列表提 PR |
| 2 | `marketing/hackaday-project.md` | Hackaday.io 项目页 |
| 3 | `marketing/reddit-post.md` | r/RFID、r/NFC（先看版规） |
| 4 | `marketing/producthunt.md` | Product Hunt 发布 |
| 5 | `marketing/seo-keywords.md` | 官网选题排期 |

---

## 常见报错

| 报错 | 原因 | 解决 |
| --- | --- | --- |
| `remote: Repository not found` | 远程地址用户名写错，或仓库没建 | 核对 `git remote -v` |
| `failed to push some refs` | 网页建仓时勾了 README | 先 `git pull --rebase origin main` |
| `Authentication failed` | 浏览器登录没完成 | 重新 `git push`，或 `git config --global credential.helper manager` |
| CI 红叉 | 缺 `ruff`/`pytest` | 已写在 `pyproject.toml` 的 dev 依赖里，`pip install -e ".[dev]"` |
