"""Minimal example: enumerate readers and read a tag UID.

Runs against any reader whose serial protocol is documented as line-based
(most vendor CLI bridges). Adapt the frame strings to your device manual.

    python examples/python/read_tag.py COM5
"""

import sys

from rfidtoolkit import Device, format_uid


def main(port: str) -> int:
    dev = Device(port, baudrate=115200, timeout=2.0)
    with dev:
        dev.send(b"uid\r\n")
        for line in dev.iter_lines():
            if not line:
                continue
            parts = line.split()
            try:
                uid = bytes(int(p, 16) for p in parts)
            except ValueError:
                continue
            if len(uid) >= 4:
                print(f"UID: {format_uid(uid)}  ({len(uid)} bytes)")
                return 0
    print("No tag response received. Check antenna position and power.")
    return 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
