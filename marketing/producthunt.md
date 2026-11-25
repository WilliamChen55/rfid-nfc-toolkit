# Product Hunt 发布文案

**Name**
```
RFID/NFC Toolkit
```

**Tagline (60 chars max)**
```
Identify and decode RFID tags in Python — no vendor GUI
```

**Description**
```
A cross-platform Python toolkit for reading, identifying and analyzing RFID/NFC tags on hardware
you own or are authorized to test.

Point it at your reader and get the protocol layer: ATQA/SAK decoding for ISO/IEC 14443-A, ATQB
parsing for 14443-B, ISO 15693 inventory, CRC-A/CRC-B helpers, UID formatting, and JSON output you
can drop into an inventory or asset-management pipeline.

Works over USB serial and PC/SC on Windows, macOS and Linux. Ships a machine-readable hardware
compatibility matrix (Proxmark3, ACR122U, PN532, Flipper Zero, Chameleon Ultra, iCopy-XS).

Built for hardware developers and engineers who need the bytes, not a screenshot. Read / identify /
analyze only — no key recovery, credential recovery or duplication, with an explicit acceptable-use
notice in the repo.
```

**First comment（发布者自己置顶）**
```
Author here. The motivation was simple: every reader has a proprietary GUI and none of them expose
frames in a consistent shape, so cross-device comparison was impossible on our team.

Happy to answer anything about protocol decoding, serial transports, or where the compatibility
matrix needs more devices. If you test a reader we don't list, the issue template takes 2 minutes.
```

**Topics**
```
Developer Tools · Hardware · Open Source · Security
```

**Links**
- Website: https://hackerwarehouse.me
- GitHub: https://github.com/WilliamChen55/rfid-nfc-toolkit
- Docs: https://WilliamChen55.github.io/rfid-nfc-toolkit/

**Gallery 建议 4 张**（做图时用"研究/开发"口径，不出现操作结果）
1. CLI 输出截图（devices + identify --json）
2. 协议表/兼容矩阵的可读化卡片
3. 实物 + 电脑连接的场景照（手持标签、罪案不出现他人卡片特写）
4. README 首屏与架构图

**避坑**
- Product Hunt 社区对"hacking tool"敏感，文案里一律用 research / development / identify
- 不要写"支持所有卡";不要承诺"复制"；不投"security bypass"
