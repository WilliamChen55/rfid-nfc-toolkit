"""Device discovery and a thin serial transport layer.

The transport is intentionally generic: subclasses in the community wrap
specific reader protocols (vendor CLI bridges, CDC-ACM serial, etc.).
Nothing here performs credential recovery.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Iterator, List, Optional

try:  # pragma: no cover - optional dependency at runtime
    from serial.tools import list_ports
except Exception:  # pragma: no cover
    list_ports = None


KNOWN_USB_IDS = {
    (0x1D6B, 0x0001): "Generic CDC-ACM serial",
    (0x2E8A, 0x0005): "Raspberry Pi Pico (CDC)",
    (0x0483, 0x5740): "STM32 Virtual COM Port",
    (0x04D8, 0xE7A0): "Microchip CDC",
    (0x0403, 0x6001): "FTDI FT232",
}


@dataclass
class DeviceInfo:
    port: str
    description: str
    hwid: str
    serial_number: Optional[str] = None
    vendor: str = "unknown"

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)


class Device:
    """Represents an attached reader/writer reachable over a serial port."""

    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 1.0):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self._serial = None

    # -- discovery ----------------------------------------------------------

    @classmethod
    def discover(cls) -> List["DeviceInfo"]:
        if list_ports is None:
            return []
        infos: List[DeviceInfo] = []
        for p in list_ports.comports():
            vendor = "unknown"
            if p.vid is not None and p.pid is not None:
                vendor = KNOWN_USB_IDS.get((p.vid, p.pid), f"{p.vid:04X}:{p.pid:04X}")
            infos.append(
                DeviceInfo(
                    port=p.device,
                    description=p.description or "",
                    hwid=p.hwid or "",
                    serial_number=getattr(p, "serial_number", None),
                    vendor=vendor,
                )
            )
        return infos

    @classmethod
    def autodetect(cls, baudrate: int = 115200) -> Optional["Device"]:
        infos = cls.discover()
        if not infos:
            return None
        return cls(infos[0].port, baudrate=baudrate)

    # -- transport ----------------------------------------------------------

    def open(self) -> None:
        if self._serial is None:
            import serial  # local import keeps discovery usable without pyserial

            self._serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)

    def close(self) -> None:
        if self._serial is not None:
            self._serial.close()
            self._serial = None

    def __enter__(self) -> "Device":
        self.open()
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    def send(self, frame: bytes) -> None:
        if self._serial is None:
            raise RuntimeError("Device is not open")
        self._serial.write(frame)

    def read(self, size: int = 64) -> bytes:
        if self._serial is None:
            raise RuntimeError("Device is not open")
        return self._serial.read(size)

    def iter_lines(self) -> Iterator[str]:
        if self._serial is None:
            raise RuntimeError("Device is not open")
        while True:
            line = self._serial.readline()
            if not line:
                return
            yield line.decode("utf-8", errors="replace").strip()
