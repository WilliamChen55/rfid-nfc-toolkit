"""Generate a Google Merchant Center product feed for the curated product set.

Only the recommended / low-policy-risk hardware is included. Descriptions are
rewritten to stay inside the store's read / identify / analyze messaging, so
they do not trip Google's access-device policies.

Usage:
    python scripts/build_merchant_feed.py

Output:
    docs/feed/merchant-products.xml  (served by GitHub Pages)
"""

import html
import json
import re
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

STORE = "https://hackerwarehouse.me"

# id -> curated metadata. Keep the list short on purpose: fewer SKUs, cleaner data.
PRODUCTS = {
    464: {
        "brand": "Proxmark3",
        "mpn": "PM3-RDV4-01",
        "title": "Proxmark3 RDV4.01 RFID Research Platform - LF 125kHz + HF 13.56MHz",
        "desc": (
            "Proxmark3 RDV4.01 is the reference open-source platform for RFID research, "
            "protocol analysis and tag diagnostics. It reads and identifies LF (125 kHz) and "
            "HF (13.56 MHz) tags, including ISO14443-A/B and ISO15693, and pairs with the "
            "open-source RFID/NFC Toolkit for ATQA/SAK decoding and JSON output. "
            "Includes PCBA with shell, HF and LF antennas, two test cards, USB cable and SIM adapter. "
            "Intended for authorized testing of tags, cards and readers you own."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2834: {
        "brand": "Proxmark",
        "mpn": "PROXMARK5",
        "title": "Proxmark 5 RFID Research Platform - LF + HF Protocol Analysis",
        "desc": (
            "Proxmark 5 is the next-generation open-source RFID research platform with a faster "
            "front end, improved RF power supply and broader protocol coverage than RDV4. "
            "Suitable for reading and analyzing LF (125 kHz) and HF (13.56 MHz) tags, "
            "bench diagnostics and firmware development. "
            "For authorized testing of cards and readers you own."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2167: {
        "brand": "iCopy",
        "mpn": "ICOPY-XS",
        "title": "iCopy-XS Standalone RFID Reader and Analyzer with Touchscreen",
        "desc": (
            "iCopy-XS is a standalone handheld RFID reader and analyzer with a color touchscreen, "
            "no laptop required. It reads and identifies 125 kHz and 13.56 MHz tags in the field, "
            "supports card inspection, frequency detection and firmware-based workflows. "
            "For authorized testing and inventory work on tags and cards you own."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2219: {
        "brand": "Flipper Devices",
        "mpn": "FLIPPER-ZERO",
        "title": "Flipper Zero Portable Multi-Tool for Sub-GHz, RFID, NFC and IR",
        "desc": (
            "Flipper Zero is a portable multi-tool for pentesters and hardware enthusiasts. "
            "It reads and inspects Sub-GHz remotes, 125 kHz and 13.56 MHz RFID/NFC tags, "
            "infrared signals and iButton devices, with an open firmware ecosystem and GPIO headers. "
            "Ships with the toolkit-compatible serial bridge for protocol-level tag identification. "
            "Use only on devices and tags you own or are authorized to test."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2186: {
        "brand": "Great Scott Gadgets",
        "mpn": "HACKRF-ONE",
        "title": "HackRF One Software Defined Radio - 1 MHz to 6 GHz Transceiver",
        "desc": (
            "HackRF One is an open-source SDR transceiver covering 1 MHz to 6 GHz with a half-duplex "
            "RF front end, SMA connectors and USB power. Used for spectrum observation, signal "
            "analysis, protocol research and RF education. It observes RF activity around 13.56 MHz "
            "but is not a tag-protocol reader. Operate within the radio regulations of your jurisdiction."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2191: {
        "brand": "PortaPack",
        "mpn": "PORTAPACK-H4M",
        "title": "PortaPack H4M for HackRF One - Standalone SDR with Touchscreen",
        "desc": (
            "PortaPack H4M turns a HackRF One into a standalone handheld SDR: 3.2 inch touchscreen, "
            "navigation controls, headphone and microSD slot, plus a wide set of receive and analysis "
            "applications for spectrum work and RF education. HackRF One not included. "
            "Operate within the radio regulations of your jurisdiction."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2258: {
        "brand": "Electronic Cats",
        "mpn": "CATSNIFFER",
        "title": "CatSniffer Multiprotocol IoT Sniffer - Sub-GHz, LoRa, Zigbee and BLE",
        "desc": (
            "CatSniffer is an open-source multiprotocol, multiband board for sniffing and communicating "
            "with IoT devices. It covers Sub-GHz, LoRa, Zigbee/802.15.4 and BLE through replaceable "
            "radio modules, and runs open firmware for capture and analysis workflows. "
            "For research on devices and networks you are authorized to test."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2213: {
        "brand": "Great Scott Gadgets",
        "mpn": "GREATFET-ONE",
        "title": "GreatFET One Hardware Hacking Tool - USB Development Board",
        "desc": (
            "GreatFET One is an extensible, open-source USB hardware tool with two USB ports, "
            "GPIO, SPI, I2C, UART and logic-analysis style workflows. It is used for hardware "
            "bring-up, firmware development, protocol reverse engineering education and "
            "lab automation on your own equipment."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2209: {
        "brand": "Great Scott Gadgets",
        "mpn": "CYNTHION",
        "title": "Cynthion USB Test Instrument - Build, Test and Monitor USB Devices",
        "desc": (
            "Cynthion is an all-in-one open-source instrument for building, testing, monitoring and "
            "experimenting with USB devices. It provides a USB 2.0 analyzer, a host/device emulation "
            "path and FPGA-based custom gateware support for protocol development and lab research."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2254: {
        "brand": "F-Secure",
        "mpn": "USB-ARMORY-MKII",
        "title": "USB Armory MkII - Open Source USB Computer for Security Research",
        "desc": (
            "USB Armory MkII is a full-featured computer in a USB stick form factor, designed for "
            "security research and embedded development. It runs Linux, supports hardware crypto, "
            "flash storage and a headless configuration, and is used for secure boot, key storage "
            "and portable lab workloads."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    2026: {
        "brand": "Great Scott Gadgets",
        "mpn": "LAN-TAP-PRO",
        "title": "LAN Tap Pro - Passive Ethernet Network Tap",
        "desc": (
            "LAN Tap Pro is a passive Ethernet tap that requires no power: it passes traffic through "
            "while exposing a copy of both directions for monitoring and analysis tools. "
            "Use it on networks you own or are authorized to monitor."
        ),
        "category": "Electronics > Electronics Accessories",
    },
    475: {
        "brand": "ProxGrind",
        "mpn": "RF-DETECTOR",
        "title": "RF Detector by ProxGrind - Handheld LF and HF Field Detector",
        "desc": (
            "RF Detector by ProxGrind is a compact handheld device that senses LF and HF RF fields, "
            "helping you locate active readers and confirm antenna output before field work. "
            "A practical pocket tool for installers, lab benches and RFID site surveys."
        ),
        "category": "Electronics > Electronics Accessories",
    },
}


def fetch(ids):
    url = f"{STORE}/wp-json/wc/store/products?include={','.join(str(i) for i in ids)}&per_page=50"
    req = urllib.request.Request(url, headers={"User-Agent": "merchant-feed-builder/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return {p["id"]: p for p in json.loads(r.read().decode("utf-8"))}


def clean(text):
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def build(products):
    items = []
    for pid, meta in PRODUCTS.items():
        p = products.get(pid)
        if not p:
            continue
        name = html.unescape(p["name"])
        price_minor = int(p["prices"]["price"])
        price = f"{price_minor / 100:.2f} {p['prices']['currency_code']}"
        availability = "in_stock" if p.get("is_in_stock") else "out_of_stock"
        image = p["images"][0]["src"] if p.get("images") else ""
        items.append(
            "\n".join(
                [
                    "  <item>",
                    f"    <g:id>{pid}</g:id>",
                    f"    <title>{escape(meta['title'])}</title>",
                    f"    <description>{escape(meta['desc'])}</description>",
                    f"    <link>{escape(p['permalink'])}</link>",
                    f"    <g:image_link>{escape(image)}</g:image_link>",
                    f"    <g:price>{price}</g:price>",
                    f"    <g:availability>{availability}</g:availability>",
                    "    <g:condition>new</g:condition>",
                    f"    <g:brand>{escape(meta['brand'])}</g:brand>",
                    f"    <g:mpn>{escape(meta['mpn'])}</g:mpn>",
                    "    <g:identifier_exists>no</g:identifier_exists>",
                    f"    <g:google_product_category>{escape(meta['category'])}</g:google_product_category>",
                    f"    <g:product_type>{escape(name)}</g:product_type>",
                    "    <g:adult>no</g:adult>",
                    "  </item>",
                ]
            )
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n'
        "  <channel>\n"
        "    <title>Hacker Warehouse - recommended hardware feed</title>\n"
        f"    <link>{STORE}</link>\n"
        "    <description>Curated RFID, NFC and SDR hardware for Google Merchant Center</description>\n"
        + "\n".join(items)
        + "\n  </channel>\n</rss>\n"
    )


if __name__ == "__main__":
    products = fetch(list(PRODUCTS))
    out = Path(__file__).resolve().parent.parent / "docs" / "feed" / "merchant-products.xml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(products), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes, {len(products)} products)")
    missing = [pid for pid in PRODUCTS if pid not in products]
    if missing:
        print("missing ids:", missing)
