# RFID/NFC Toolkit

[![Store](https://img.shields.io/badge/Hardware-hackerwarehouse.me-0b7285?style=for-the-badge)](https://hackerwarehouse.me)
[![CI](https://github.com/WilliamChen55/rfid-nfc-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/WilliamChen55/rfid-nfc-toolkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Protocols](https://img.shields.io/badge/ISO%2FIEC-14443A%20%7C%2014443B%20%7C%2015693-informational)](docs/protocols.md)

**Hardware, firmware and accessories: [hackerwarehouse.me](https://hackerwarehouse.me)**

A cross-platform Python toolkit for **reading, identifying and analyzing** RFID/NFC tags on your own hardware. Built for hardware developers, engineering teams and security researchers who need protocol-level visibility instead of vendor-locked GUIs.

> **Legal Notice**
> This project is intended for authorized research, development, testing and diagnostics on tags, cards and readers that you own or have explicit written permission to test. It is a **read/identify/analysis** toolkit: it does not implement key recovery, credential recovery, access bypass or card duplication. See [LEGAL_NOTICE.md](LEGAL_NOTICE.md).

---

## Get the hardware

This toolkit is maintained alongside the reader/writer hardware lineup at **[hackerwarehouse.me](https://hackerwarehouse.me)**. Everything below is tested against devices we stock; see [docs/products.md](docs/products.md) for the full list with notes on which models fit which workflow.

| Device | Best for | Where |
| --- | --- | --- |
| Proxmark3 RDV4 | Full protocol work, LF + HF, scriptable bridge | [hackerwarehouse.me](https://hackerwarehouse.me) |
| Proxmark5 | Next-gen platform, higher throughput | [hackerwarehouse.me](https://hackerwarehouse.me) |
| iCopy-XS | Standalone field reading, no laptop required | [hackerwarehouse.me](https://hackerwarehouse.me) |
| Chameleon Ultra | Tag emulation studies, 14443A/B + 15693 | [hackerwarehouse.me](https://hackerwarehouse.me) |
| Flipper Zero | Multi-protocol bench tool, serial bridge | [hackerwarehouse.me](https://hackerwarehouse.me) |
| HackRF One + ANT500 | Spectrum observation around 13.56 MHz | [hackerwarehouse.me](https://hackerwarehouse.me) |
| ACR122U / PN532 | Cheap PC/SC and UART front ends for CI rigs | [hackerwarehouse.me](https://hackerwarehouse.me) |

> Bulk, education and lab orders: see the store's contact page. Firmware bundles and replacement antennas ship with the same part numbers used in `data/compatibility.json`.
>
> Full device guide with live product links: **[RFID / NFC Toolkit — device compatibility guide](https://hackerwarehouse.me/rfid-nfc-toolkit-compatibility/)**.

---

## Features

- **Device discovery** over USB serial across Windows, macOS and Linux
- **Tag identification** from ATQA / SAK / ATQB / system information for ISO/IEC 14443-A, 14443-B and ISO/IEC 15693
- **Protocol utilities**: CRC-A / CRC-B, UID formatting, hex normalization, SAK → tag-family mapping
- **Compatibility matrix** for common reader/writer hardware ([data/compatibility.json](data/compatibility.json))
- **CLI + Python API** — scriptable, no GUI required
- **Structured JSON output** for integration into inventory and asset-management pipelines

## Quick Start

```bash
git clone https://github.com/WilliamChen55/rfid-nfc-toolkit.git
cd rfid-nfc-toolkit
pip install -e .

# list attached reader hardware
rfidtoolkit devices

# identify a tag presented to a reader on COM5
rfidtoolkit identify --port COM5 --json
```

Python API:

```python
from rfidtoolkit import Device, decode_atqa, tag_family_from_sak

dev = Device.discover()[0]
response = dev.request_uid()
print(decode_atqa(response.atqa), tag_family_from_sak(response.sak))
```

## Supported Protocols

| Standard | Carrier | What this toolkit does |
| --- | --- | --- |
| ISO/IEC 14443-A | 13.56 MHz | ATQA/SAK decode, UID read, CRC-A, tag family classification |
| ISO/IEC 14443-B | 13.56 MHz | ATQB decode, UID read, CRC-B |
| ISO/IEC 15693 (vicinity) | 13.56 MHz | Inventory, UID read, block descriptor parsing |

> Key recovery, encryption-bypass and cloning routines are **intentionally out of scope**.

## Compatibility

See [docs/compatibility.md](docs/compatibility.md) and the machine-readable [data/compatibility.json](data/compatibility.json).
Verified on Proxmark3 RDV4 / Easy, iCopy-XS, Chameleon Ultra, ACR122U, PN532 breakout boards and Flipper Zero (serial bridge mode) — all available at [hackerwarehouse.me](https://hackerwarehouse.me).

## Documentation

- [Getting started](docs/getting-started.md)
- [Products and recommended setups](docs/products.md)
- [Protocol notes](docs/protocols.md)
- [Compatibility matrix](docs/compatibility.md)
- [FAQ](docs/faq.md)
- [Legal notice](LEGAL_NOTICE.md)

## Contributing

Bug reports, compatibility reports and hardware test results are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). If you have a device we don't support yet, open the **Hardware compatibility** issue template.

## Security

Please report vulnerabilities as described in [SECURITY.md](SECURITY.md), not in public issues.

## Store

[hackerwarehouse.me](https://hackerwarehouse.me) — readers, writers, SDR hardware, antennas and accessories for RFID/NFC engineering work in the US and EU.

Maintained by the team behind [hackerwarehouse.me](https://hackerwarehouse.me).

## License

MIT — see [LICENSE](LICENSE).
