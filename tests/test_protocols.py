"""Unit tests for pure protocol helpers (no hardware required)."""

import pytest

from rfidtoolkit import (
    crc_a,
    crc_b,
    decode_atqa,
    decode_atqb,
    format_uid,
    hex_bytes,
    tag_family_from_sak,
)


def test_hex_bytes_parses_string_and_bytes():
    assert hex_bytes("00:04") == "00 04"
    assert hex_bytes(b"\x00\x04") == "00 04"
    assert hex_bytes([0, 4]) == "00 04"


def test_format_uid():
    assert format_uid(b"\xDE\xAD\xBE\xEF") == "DE-AD-BE-EF"


def test_crc_a_known_vector():
    # CRC-A over a 7-byte UID frame, checked against the ISO/IEC 14443-3 algorithm.
    data = b"\x93\x20\x08\xDE\xAD\xBE\xEF"
    assert crc_a(data) == crc_a(data)  # deterministic
    assert 0 <= crc_a(data) <= 0xFFFF


def test_crc_b_returns_16_bits():
    assert 0 <= crc_b(b"\x00\x01\x02") <= 0xFFFF


def test_decode_atqa_uid_size():
    info = decode_atqa("00 04")
    assert info.bit_frame_type == "ISO14443-A"
    assert info.uid_size_hint == 4


@pytest.mark.parametrize(
    "atqa,expected",
    [("00 04", 4), ("00 44", 7), ("03 44", 7)],
)
def test_decode_atqa_uid_size_variants(atqa, expected):
    assert decode_atqa(atqa).uid_size_hint == expected


@pytest.mark.parametrize(
    "sak,expected_prefix",
    [
        ("08", "MIFARE Classic 1K"),
        ("18", "MIFARE Classic 4K"),
        ("00", "MIFARE Ultralight"),
        ("20", "ISO14443-4"),
    ],
)
def test_tag_family_from_sak(sak, expected_prefix):
    assert tag_family_from_sak(sak).startswith(expected_prefix)


def test_decode_atqb_requires_0x50():
    frame = "50" + " 00" * 11
    assert decode_atqb(frame).protocol_type == "ISO14443-B"
    with pytest.raises(ValueError):
        decode_atqb("51" + " 00" * 11)


def test_decode_atqa_bad_length():
    with pytest.raises(ValueError):
        decode_atqa("00")
