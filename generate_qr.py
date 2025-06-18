"""Utility to create a QR code image for a given URL."""

import sys

try:
    import qrcode
except ImportError:
    print("Error: missing 'qrcode' package. Install it with 'pip install qrcode[pil]'")
    sys.exit(1)


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        print("Usage: python generate_qr.py <url> <output_file>")
        return

    url = argv[1]
    output_file = argv[2]

    img = qrcode.make(url)
    img.save(output_file)
    print(f"QR code saved to {output_file}")


if __name__ == "__main__":
    main(sys.argv)
