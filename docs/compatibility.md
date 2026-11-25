# Compatibility Matrix

Every device listed below is stocked at [hackerwarehouse.me](https://hackerwarehouse.me); see [products.md](products.md) for buying guidance.

Machine-readable source: [../data/compatibility.json](../data/compatibility.json).
Status values: `verified` (tested by maintainers), `reported` (community report), `planned`.

| Device | Type | Frequencies | Protocols | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Proxmark3 RDV4 | Reader/writer + SDR bridge | 125 kHz, 13.56 MHz | 14443A/B, 15693, LF | verified | Use the `pm3` client bridge mode; firmware ≥ v4.19 |
| Proxmark3 Easy | Reader/writer | 125 kHz, 13.56 MHz | 14443A/B, 15693, LF | verified | Same client, smaller flash |
| iCopy-XS | Standalone reader/writer | 125 kHz, 13.56 MHz | 14443A/B, 15693 | reported | Line-based CLI bridge; firmware varies by batch |
| Chameleon Ultra | Emulator/reader | 13.56 MHz | 14443A/B, 15693 | reported | Serial protocol documented in the upstream repo |
| Flipper Zero | Multi-tool | 125 kHz, 13.56 MHz, sub-GHz | 14443A/B, 15693 | reported | Via `serial bridge` app; throughput limited |
| ACR122U | Contactless reader | 13.56 MHz | 14443A/B | verified | PC/SC; use `pyscard` backend instead of raw serial |
| PN532 breakout | NFC module | 13.56 MHz | 14443A/B, 15693 | verified | UART or I²C; HSU mode recommended |
| HackRF One | SDR | 1 MHz – 6 GHz | — | planned | Non-RFID: suitable for spectrum observation, not tag protocol work |

## Adding your device

Open a **Hardware compatibility** issue with:

1. Device model and firmware version
2. Transport (serial / PC-SC / HID bridge) and baud rate
3. `rfidtoolkit devices` output
4. A redacted sample of the response line for a tag **you own**

We do not accept reports containing third-party credential or access data.
