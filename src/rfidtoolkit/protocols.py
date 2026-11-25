"""Protocol helpers for ISO/IEC 14443 and ISO/IEC 15693.

These helpers are pure functions over raw frames returned by a reader.
They perform decoding and checksum computation only; no key recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional

# --- byte helpers -----------------------------------------------------------


def hex_bytes(data: Iterable[int] | bytes | str) -> str:
    """Return a space-separated uppercase hex string, tolerant of input formats."""
    if isinstance(data, str):
        raw = data.replace(":", " ").replace("-", " ").split()
        values = [int(x, 16) for x in raw if x]
    else:
        values = list(data)
    return " ".join(f"{v:02X}" for v in values)


@dataclass
class Uid:
    """Decoded UID with length information."""

    bytes: bytes
    length: int

    def __str__(self) -> str:
        return format_uid(self.bytes)


def format_uid(uid: bytes | Iterable[int], separator: str = "-") -> str:
    return separator.join(f"{b:02X}" for b in uid)


# --- CRC --------------------------------------------------------------------


def crc_a(data: bytes) -> int:
    """ISO/IEC 14443-A CRC (initial value 0x6363, polynomial 0x8408, reflected)."""
    crc = 0x6363
    for byte in data:
        byte ^= crc & 0xFF
        byte ^= byte << 4
        crc = (
            (crc >> 8)
            ^ (byte << 8)
            ^ (byte << 3)
            ^ (byte >> 4)
        ) & 0xFFFF
    return ((crc & 0xFF) << 8) | ((crc >> 8) & 0xFF)


def crc_b(data: bytes) -> int:
    """ISO/IEC 14443-B CRC (initial value 0xFFFF, polynomial 0x8408)."""
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0x8408
            else:
                crc >>= 1
    return crc & 0xFFFF


# --- ATQA / SAK -------------------------------------------------------------


@dataclass
class AtqaInfo:
    raw: bytes
    bit_frame_type: str
    uid_size_hint: int
    proprietary: bool


def decode_atqa(atqa: bytes | str) -> AtqaInfo:
    """Decode the 2-byte ATQA response of an ISO/IEC 14443-A tag."""
    raw = _to_bytes(atqa, expected=2)
    # The frame is transmitted LSB-first, so the 16-bit value is (byte0 << 8) | byte1.
    value = (raw[0] << 8) | raw[1]
    proprietary = bool(value & 0x0010)          # bit b5: proprietary tag
    # Bits b7..b6 encode the UID size class
    size_code = value & 0x00C0
    uid_size_hint = {0x0000: 4, 0x0040: 7, 0x0080: 10}.get(size_code, 4)
    return AtqaInfo(
        raw=raw,
        bit_frame_type="ISO14443-A",
        uid_size_hint=uid_size_hint,
        proprietary=proprietary,
    )


def tag_family_from_sak(sak: bytes | int | str) -> str:
    """Map a SAK byte to the most likely tag family."""
    value = int(sak, 16) if isinstance(sak, str) else (
        sak[0] if isinstance(sak, (bytes, bytearray)) else int(sak)
    )
    table = {
        0x00: "MIFARE Ultralight / ISO14443-3 Type A (UID only)",
        0x08: "MIFARE Classic 1K",
        0x09: "MIFARE Classic Mini",
        0x18: "MIFARE Classic 4K",
        0x10: "MIFARE Plus / ISO14443-3 Type A",
        0x20: "ISO14443-4 compliant (DESFire / CPU card)",
        0x28: "ISO 14443-4 smart card (SAK 0x28)",
        0x38: "ISO 18092 NFC / ISO14443-4 dual interface",
        0x88: "MIFARE Classic 1K (cloning-resistant variant)",
    }
    return table.get(value, f"Unknown SAK 0x{value:02X}")


@dataclass
class AtqbInfo:
    raw: bytes
    uid_size_hint: int
    protocol_type: str


def decode_atqb(atqb: bytes | str) -> AtqbInfo:
    """Decode the ATQB response of an ISO/IEC 14443-B tag (leading 0x50 byte)."""
    raw = _to_bytes(atqb, expected=12)
    if raw[0] != 0x50:
        raise ValueError("Not an ATQB frame (expected 0x50)")
    return AtqbInfo(
        raw=raw,
        uid_size_hint=4,
        protocol_type="ISO14443-B",
    )


# --- internals --------------------------------------------------------------


def _to_bytes(data: bytes | str | Iterable[int], expected: Optional[int] = None) -> bytes:
    if isinstance(data, bytes):
        out = data
    elif isinstance(data, str):
        parts = data.replace(":", " ").replace("-", " ").split()
        out = bytes(int(p, 16) for p in parts if p)
    else:
        out = bytes(data)
    if expected and len(out) != expected:
        raise ValueError(f"Expected {expected} bytes, got {len(out)}")
    return out
