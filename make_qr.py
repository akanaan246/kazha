"""Make the business-card QR code for the links page.

Usage:  python3 make_qr.py https://your-site-url/
Needs:  pip install segno
Writes: qr/kazha-qr.svg (vector, best for the printer)
        qr/kazha-qr.png (2000 px, for previews / Canva)
"""
import os
import sys

import segno

url = sys.argv[1]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr")
os.makedirs(out, exist_ok=True)

# Error level Q survives ~25% damage (scratches, a bent card). Border 4 is the
# quiet zone the QR standard requires; don't crop it off when placing the code.
qr = segno.make(url, error="q", micro=False)
qr.save(os.path.join(out, "kazha-qr.svg"), scale=10, border=4, dark="#000000", light="#ffffff")
qr.save(os.path.join(out, "kazha-qr.png"), scale=2000 // (qr.symbol_size(border=4)[0]) or 1,
        border=4, dark="#000000", light="#ffffff")
print("QR version", qr.version, "-", qr.designator, "->", url)
