"""RFID/NFC Toolkit — protocol-level utilities for authorized hardware testing.

Public API:
    from rfidtoolkit import Device, decode_atqa, tag_family_from_sak, crc_a, crc_b
"""

from .device import Device, DeviceInfo
from .protocols import (
    crc_a,
    crc_b,
    decode_atqb,
    decode_atqa,
    format_uid,
    hex_bytes,
    tag_family_from_sak,
)

__all__ = [
    "Device",
    "DeviceInfo",
    "crc_a",
    "crc_b",
    "decode_atqa",
    "decode_atqb",
    "tag_family_from_sak",
    "format_uid",
    "hex_bytes",
]

__version__ = "0.1.0"
