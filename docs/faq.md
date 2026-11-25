# FAQ

**Where can I buy the hardware?**
Readers, writers, antennas and SDR front ends are available at [hackerwarehouse.me](https://hackerwarehouse.me). The [products page](products.md) maps each device to the workflow it suits.

**Does this toolkit read or modify card contents?**
It reads public identification data (UID, ATQA, SAK, ATQB, system information) and analyzes frames. It does not perform key recovery, credential recovery or duplication.

**Which readers work out of the box?**
Any device exposing a serial or PC/SC interface with a documented, line-based or APDU transport. See the [compatibility matrix](compatibility.md).

**Why does my tag show no response?**
Usually antenna coupling: metal nearby, stacked cards, or distance. Try a known-good tag, then move the tag slowly across the antenna.

**Does it work on macOS on Apple Silicon?**
Yes — `pyserial` ships universal wheels. FTDI-based adapters need the vendor driver.

**Can I use it with an SDR like HackRF?**
HackRF is a general-purpose SDR; it can observe spectrum but is not a tag-protocol reader. Use a dedicated 13.56 MHz front end for tag work.

**Is commercial use allowed?**
The MIT licence permits it. Regulatory obligations (type approval, import registration, radio rules) remain yours.

**Can I get support for a device I resell?**
Open a Hardware compatibility issue and include the transport details; maintainers and community members can add a driver adapter.

**Where do I report a bug?**
Use the bug report template under Issues. For security issues, follow [SECURITY.md](../SECURITY.md).
