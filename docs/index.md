# RFID/NFC Toolkit — documentation

**Hardware: [hackerwarehouse.me](https://hackerwarehouse.me)**

A Python toolkit for reading, identifying and analyzing RFID/NFC tags on hardware you own or are authorized to test.

- [Getting started](getting-started.md)
- [Products and recommended setups](products.md)
- [Protocol notes](protocols.md)
- [Compatibility matrix](compatibility.md)
- [FAQ](faq.md)
- [Legal notice](../LEGAL_NOTICE.md)

```{toctree}
:hidden:

getting-started
products
protocols
compatibility
faq
```

## What it does

- Enumerates attached readers over serial / PC-SC
- Identifies tags from ATQA, SAK, ATQB and ISO 15693 system information
- Provides CRC-A, CRC-B and UID formatting utilities
- Emits JSON for inventory and asset-management pipelines

## What it does not do

- Key or credential recovery
- Card duplication or emulation of third-party credentials
- Access-control bypass

See [LEGAL_NOTICE.md](../LEGAL_NOTICE.md) before deploying in a commercial environment.
