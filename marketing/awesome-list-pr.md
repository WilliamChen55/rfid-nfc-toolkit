# 提交到 Awesome 列表的 PR 文案

> 一次只加一行，不要一次塞多个仓库。下面按目标列表给了可直接用的段落。

---

## 目标 1：`awesome-security`（或 `awesome-hardware`）

**PR 标题**

```
Add rfid-nfc-toolkit to Hardware Security Tools
```

**PR 描述**

```
### What
[rfid-nfc-toolkit](https://github.com/WilliamChen55/rfid-nfc-toolkit) — a cross-platform Python
toolkit for reading, identifying and analyzing RFID/NFC tags (ISO/IEC 14443-A/B, ISO/IEC 15693)
on hardware you own or are authorized to test.

### Why it fits this list
- Protocol-level decoding (ATQA/SAK/ATQB, CRC-A/CRC-B) in plain Python, no vendor GUI required
- Works across Windows/macOS/Linux over USB serial and PC/SC
- Ships a hardware compatibility matrix covering Proxmark3, ACR122U, PN532, Flipper Zero, iCopy-XS,
  Chameleon Ultra
- MIT licensed, CI-tested, read/identify scope only — no duplication or key-recovery code

### Checklist
- [x] Actively maintained
- [x] Documented (`docs/`)
- [x] Open source licence (MIT)
```

---

## 目标 2：`awesome-rfid` / `awesome-nfc`（若已有独立列表）

**表格行（插到 Tools 分类）**

```
| [rfid-nfc-toolkit](https://github.com/WilliamChen55/rfid-nfc-toolkit) | Python toolkit for tag identification and protocol decoding (14443A/B, 15693) | MIT |
```

---

## 目标 3：`awesome-sdr`（旁证/生态位）

**一句话**

```
- [rfid-nfc-toolkit](https://github.com/WilliamChen55/rfid-nfc-toolkit) — protocol-layer companion for
  RFID/NFC front ends when a general-purpose SDR is used for spectrum observation.
```

---

## 提 PR 的注意事项

1. 先读 `CONTRIBUTING.md` 和现有条目格式，**严格照抄排版**（有没有句号、链接顺序、描述长度）
2. 一次性改一个文件、一行；多个列表就开多个 PR
3. 描述里不出现 clone / crack / bypass / clone cards 这类词
4. 如果列表要求"至少 N stars"，先把 star 数做起来再去提，否则会被直接关
