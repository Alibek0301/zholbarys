# zholbarys

## Generate QR code
Install the `qrcode` package with Pillow support using:

```bash
python3 -m pip install qrcode[pil]
```

Then run the script to create a PNG image:

```bash
python3 generate_qr.py <url> output.png
```

If you encounter a `ModuleNotFoundError`, ensure the `qrcode` package is installed.

The website also includes a button that reveals a downloadable QR image of the current page.
