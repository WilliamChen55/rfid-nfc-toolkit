# Hackaday.io 项目页文案

**Project name**
```
RFID/NFC Toolkit — protocol-level tag identification in Python
```

**Summary (≤ 160 chars)**
```
Cross-platform Python toolkit that reads and identifies RFID/NFC tags over USB serial — built for developers and hardware engineers.
```

**Description**

```
## What it is

A Python toolkit for reading, identifying and analyzing RFID/NFC tags on hardware you own or are
authorized to test. It talks to your existing reader over USB serial or PC/SC and gives you the
protocol layer in plain Python: ATQA/SAK decoding, ATQB parsing, ISO 15693 inventory, CRC-A/CRC-B,
UID formatting, and JSON output you can pipe into an inventory pipeline.

## Why I built it

Most readers ship a vendor GUI that hides the frames. If you are integrating RFID into an
asset-management system, writing firmware, or teaching the protocol, you want the bytes, not a
screenshot. This toolkit exposes them and stays out of the way.

## Hardware

Verified against Proxmark3 RDV4, ACR122U, PN532 breakouts; community reports for iCopy-XS,
Chameleon Ultra and Flipper Zero serial bridge. Compatibility matrix is machine-readable and
open to PRs.

Everything in the matrix is stocked at hackerwarehouse.me (readers, antennas, SDR front ends).

## Scope

Read, identify, analyze. No key recovery, no credential recovery, no duplication. There is an
explicit Acceptable Use notice in the repo — this is for engineers testing their own infrastructure.

## Try it

    pip install -e .
    rfidtoolkit devices
    rfidtoolkit identify --port COM5 --json

Code: https://github.com/WilliamChen55/rfid-nfc-toolkit
Docs: https://WilliamChen55.github.io/rfid-nfc-toolkit/
Hardware: https://hackerwarehouse.me

## What's next

- HF/LF front-end adapters for more vendor bridges
- Block descriptor parsing for ISO 15693 asset tags
- A comparison harness for reader sensitivity and read range
```

**Tags**
```
rfid, nfc, python, hardware, tool, security research, iso14443, iso15693
```

**发布时的第一条 update（用于进 feed）**
```
v0.1.0 is up. ISO14443-A/B identification, ISO15693 inventory, CRC helpers, JSON output, and a
machine-readable hardware compatibility matrix. Looking for compatibility reports from anyone
running a reader we don't list yet.
```
