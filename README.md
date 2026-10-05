# Kazha — links page

The page people land on when they scan the QR code on the Kazha business card.

Live at: https://akanaan246.github.io/kazha/

## Change a link
Open `index.html`, find the **EDIT YOUR LINKS HERE** list near the bottom,
paste the full profile link between the quotes, and commit. An empty `""` hides that button.
The QR code never needs to change: it points at the page, not at the links.

## Add a logo
Upload a file named `logo.png` (transparent background works best) to this repo.

## QR code
`qr/` holds the print files. Rebuild with `python3 make_qr.py https://akanaan246.github.io/kazha/`
(needs `pip install segno`).
