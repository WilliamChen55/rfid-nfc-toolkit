# Getting Started

## Requirements

- Python 3.9+
- A USB-attached reader/writer (CDC-ACM serial, FTDI, or a vendor CLI bridge)
- Drivers for your adapter (FTDI VCP or CH340 on Windows; built-in on macOS/Linux)

## Install

```bash
git clone https://github.com/WilliamChen55/rfid-nfc-toolkit.git
cd rfid-nfc-toolkit
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Verify the device is seen

```bash
rfidtoolkit devices
rfidtoolkit devices --json
```

Expected output lists port, vendor and description. If nothing appears:

| Symptom | Fix |
| --- | --- |
| Port missing on Windows | Install FTDI VCP / CH340 driver, re-plug, check Device Manager |
| `Permission denied` on Linux | `sudo usermod -aG dialout $USER`, then re-login |
| Device present but silent | Confirm baud rate matches firmware (default 115200) |

## Identify a tag

Present a tag **you own** to the reader:

```bash
rfidtoolkit identify --port COM5 --once
rfidtoolkit identify --port /dev/ttyACM0 --json
```

Offline decoding also works without hardware:

```bash
rfidtoolkit decode --atqa "00 04" --sak 08
```

## Python API

```python
from rfidtoolkit import Device

info = Device.discover()
print(info[0].port, info[0].vendor)
```

## Next steps

- Protocol notes: [protocols.md](protocols.md)
- Compatibility: [compatibility.md](compatibility.md)
- Troubleshooting: [faq.md](faq.md)
