import qrcode
import sys

if len(sys.argv) != 3:
    print("Usage: python generate_qr.py <url> <output_file>")
    sys.exit(1)

url = sys.argv[1]
output = sys.argv[2]

img = qrcode.make(url)
img.save(output)
print(f"QR code saved to {output}")
