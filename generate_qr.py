"""Utility to create a QR code image for a given URL."""

from __future__ import annotations

import sys

try:
    import qrcode
except ImportError as exc:  # pragma: no cover - graceful runtime message
    print(
        "Error: missing dependency 'qrcode'.\n"
        "Install it via 'pip install qrcode[pil]' and try again."
    )
    raise SystemExit(1) from exc


def main(argv: list[str] | None = None) -> None:
    args = sys.argv if argv is None else argv
    if len(args) != 3:
        print("Usage: python generate_qr.py <url> <output_file>")
        return

    url = args[1]
    output_file = args[2]

    img = qrcode.make(url)
    img.save(output_file)
    print(f"QR code saved to {output_file}")


if __name__ == "__main__":
    main()
