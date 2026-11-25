"""Command line interface: `rfidtoolkit devices` / `rfidtoolkit identify`."""

from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional

from .device import Device
from .protocols import decode_atqa, hex_bytes, tag_family_from_sak


def _cmd_devices(args: argparse.Namespace) -> int:
    infos = [i.to_json() for i in Device.discover()]
    if args.json:
        print("[" + ",".join(infos) + "]")
    else:
        if not infos:
            print("No serial devices found. Check the USB cable and driver.")
            return 1
        for i in Device.discover():
            print(f"{i.port:<12} {i.vendor:<28} {i.description}")
    return 0


def _cmd_identify(args: argparse.Namespace) -> int:
    dev = Device(args.port, baudrate=args.baudrate)
    with dev:
        dev.send(b"identify\r\n")
        for line in dev.iter_lines():
            line = line.strip()
            if not line:
                continue
            if args.json:
                print(json.dumps({"raw": line}))
            else:
                print(line)
            if args.once:
                break
    return 0


def _cmd_decode(args: argparse.Namespace) -> int:
    result = {"atqa": None, "sak": None, "family": None}
    if args.atqa:
        info = decode_atqa(args.atqa)
        result["atqa"] = {
            "raw": hex_bytes(info.raw),
            "bit_frame_type": info.bit_frame_type,
            "uid_size_hint": info.uid_size_hint,
        }
    if args.sak:
        result["sak"] = hex_bytes([int(args.sak, 16)])
        result["family"] = tag_family_from_sak(args.sak)
    print(json.dumps(result, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rfidtoolkit",
        description="Read, identify and analyze RFID/NFC tags on hardware you are authorized to test.",
    )
    parser.add_argument("--version", action="version", version="rfidtoolkit 0.1.0")
    sub = parser.add_subparsers(dest="command", required=True)

    p_dev = sub.add_parser("devices", help="List attached reader hardware")
    p_dev.add_argument("--json", action="store_true")
    p_dev.set_defaults(func=_cmd_devices)

    p_id = sub.add_parser("identify", help="Identify a tag presented to a reader")
    p_id.add_argument("--port", required=True, help="Serial port, e.g. COM5 or /dev/ttyACM0")
    p_id.add_argument("--baudrate", type=int, default=115200)
    p_id.add_argument("--json", action="store_true")
    p_id.add_argument("--once", action="store_true", help="Stop after the first response")
    p_id.set_defaults(func=_cmd_identify)

    p_dec = sub.add_parser("decode", help="Decode recorded ATQA/SAK values offline")
    p_dec.add_argument("--atqa", help="ATQA hex, e.g. '00 04'")
    p_dec.add_argument("--sak", help="SAK hex, e.g. 08")
    p_dec.set_defaults(func=_cmd_decode)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
