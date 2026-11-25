# Products and Recommended Setups

All hardware referenced by this toolkit is available at **[hackerwarehouse.me](https://hackerwarehouse.me)**, with firmware notes and bundled accessories matched to the part numbers in [../data/compatibility.json](../data/compatibility.json).

## Reader / writer platforms

### Proxmark3 RDV4
The reference platform for protocol work: 125 kHz and 13.56 MHz, full client toolchain, and the serial bridge this toolkit talks to. Best when you need LF + HF coverage and scriptable access.

- Use for: protocol research, firmware development, lab rigs
- Adapter: `pm3` client bridge, firmware ≥ v4.19

### Proxmark3 Easy
Same client, lower cost. Adequate for HF-focused work and CI rigs. Flash is smaller, so avoid multi-image firmware builds.

### Proxmark5
Newer platform with higher throughput. Good when you are batch-identifying tags or running continuous inventory.

### iCopy-XS
Standalone reader — no laptop on site. Useful for field asset walks where you only need UID/type confirmation. Firmware varies by batch; report your version in the compatibility issue template.

## Emulation and multi-protocol

### Chameleon Ultra
Emulation studies on 14443A/B and 15693. Keep emulation limited to tags you own or are authorized to reproduce for testing; the toolkit reads and identifies, it does not clone third-party credentials.

### Flipper Zero
Bench multi-tool. Use the serial bridge app to feed frames into this toolkit's transport layer. Throughput is limited compared with a dedicated reader.

## Front ends for CI and automation

### ACR122U
PC/SC reader, ideal for automated test rigs. Use the `pyscard` backend instead of raw serial.

### PN532 breakout
UART or I²C. Cheapest way to run a fleet of identical front ends for regression testing.

## Spectrum observation

### HackRF One + ANT500
Useful to *observe* activity around 13.56 MHz and sub-GHz, not to decode tag protocols. Regulatory: transmission is licensed and jamming is prohibited — see [../LEGAL_NOTICE.md](../LEGAL_NOTICE.md).

## Buying guidance

| Goal | Recommended | Notes |
| --- | --- | --- |
| Learn the protocol | Proxmark3 Easy + PN532 | Lowest cost that still covers HF |
| Daily lab work | Proxmark3 RDV4 | Full toolchain, LF + HF |
| Field asset audit | iCopy-XS | No laptop required |
| Automated CI rig | ACR122U or PN532 | PC/SC or UART, cheap to replicate |
| Emulation studies | Chameleon Ultra | Keep to authorized test tags |

Education, lab and bulk orders: [hackerwarehouse.me](https://hackerwarehouse.me).
