# zholbarys

## Generate QR code
Install the `qrcode` package with Pillow support using:

```bash
pip install qrcode[pil]
```

Then run the script to create a PNG image:

```bash
python3 generate_qr.py <url> output.png
```

The website also includes a button that reveals a downloadable QR image of the current page.
