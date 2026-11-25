# Reddit 发帖文案（r/RFID / r/NFC / r/hardware）

> 先读版规。r/RFID 与 r/NFC 对"工具推广"敏感：**发帖要做成技术分享，链接放文末**。
> 不要在标题里出现 clone / crack / bypass / read any card。

---

## 版本 1：技术分享型（推荐，最不容易被删）

**Title**
```
Built a small Python library that decodes ATQA/SAK from any serial reader — feedback welcome
```

**Body**
```
I kept running into the same problem: every reader has its own GUI and none of them show you the
frames. So I wrote a thin Python layer that talks to the reader over USB serial (or PC/SC) and
gives you the protocol bits directly.

What it does:
- enumerates readers (`rfidtoolkit devices`)
- identifies tags: ATQA/SAK decode for 14443-A, ATQB for 14443-B, inventory for ISO 15693
- CRC-A / CRC-B helpers, UID formatting, JSON output for pipelines

What it deliberately doesn't do: key recovery, credential recovery, duplication. This is for
people testing their own tags and integrating RFID into inventory/asset systems.

Verified on Proxmark3 RDV4/Easy, ACR122U, PN532. Compatibility matrix is a JSON file in the repo
and I'd like to add more devices.

Repo: https://github.com/WilliamChen55/rfid-nfc-toolkit

Two things I'd like feedback on:
1. Is the SAK → family mapping missing anything common you run into?
2. Anyone got a clean way to handle 15693 block descriptors across vendors?

Disclosure: I run hackerwarehouse.me, which stocks most of the readers in the compatibility matrix.
The library is MIT and works with whatever hardware you already have.
```

---

## 版本 2：提问型（评论量更高，转化慢）

**Title**
```
How do you dump ATQA/SAK from your reader without the vendor GUI?
```

**Body**
```
Trying to standardise the tooling across a few different readers (Proxmark3, ACR122U, PN532).
Right now everyone on the team uses a different GUI and we can't compare results.

I ended up writing a small Python wrapper so the output is consistent — device list, ATQA, SAK,
UID, JSON out. Curious whether others solved this differently, or just scripted each vendor CLI.

Repo if useful: https://github.com/WilliamChen55/rfid-nfc-toolkit

(Disclosure: I run hackerwarehouse.me, the shop that stocks the readers listed there. The library
itself is MIT and hardware-agnostic.)
```

---

## 发布纪律

- 一个 subreddit 一次，**不要跨版连发**（会被判 spam）
- 账号要有历史互动，新号首发推广基本被删
- 前 30 分钟有人提问就认真回，评论活跃度决定帖子活多久
- 帖子里不要放折扣、价格、购买链接；只放 GitHub
