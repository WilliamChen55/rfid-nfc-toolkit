# Protocol Notes

Reference material for interpreting frames returned by a reader. This page documents **decoding**, not credential recovery.

## ISO/IEC 14443-A

| Field | Length | Notes |
| --- | --- | --- |
| ATQA | 2 bytes | Response to REQA/WUPA; encodes UID size class and bit-frame type |
| SAK | 1 byte | Selected Acknowledge, describes the tag family / cascade level |
| UID | 4 / 7 / 10 bytes | Cascade levels CL1 → CL3 |

### ATQA interpretation

- Byte 1 bits b7–b6 = `01` for 14443-A
- Bit `0x10` in byte 2 = proprietary tag
- UID size class: 4-byte (single), 7-byte (double), 10-byte (triple) cascade

### SAK → family (common values)

| SAK | Family |
| --- | --- |
| 0x00 | Ultralight / Type A UID only |
| 0x08 | MIFARE Classic 1K |
| 0x09 | MIFARE Classic Mini |
| 0x18 | MIFARE Classic 4K |
| 0x20 | ISO14443-4 compliant (DESFire, CPU card) |
| 0x28 | ISO14443-4 smart card |

### CRC-A

Initial value `0x6363`, reflected polynomial `0x8408`, result byte-swapped before transmission. See `rfidtoolkit.protocols.crc_a`.

## ISO/IEC 14443-B

- ATQB starts with `0x50`
- PUPI 4 bytes, application data 4 bytes, protocol info 1 byte
- CRC-B: init `0xFFFF`, polynomial `0x8408`, no final swap

## ISO/IEC 15693 (vicinity)

- Inventory via `Inventory` / `InventoryRead` commands
- UID is 8 bytes, LSB-first on air
- `Get System Information` returns block size and memory layout — useful for asset tagging projects

## Practical notes

- Antenna detuning caused by metal or stacking is the most common cause of "no response"
- Field strength drops sharply with distance; 13.56 MHz tags typically need < 5 cm on handheld readers
- Always keep a known-good reference tag for field verification

## Regulatory

Transmission is regulated. Ensure your device holds required type approval and that operation complies with local radio rules. See [../LEGAL_NOTICE.md](../LEGAL_NOTICE.md).
