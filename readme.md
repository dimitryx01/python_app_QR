# Python QR Generator — Branded QR with Center Logo (Fundación Kālida)

A specialized Python project designed to generate **custom branded QR codes**. This tool was specifically developed for **Fundación Kālida** to create high-quality, brand-aligned QR codes for their digital and physical assets.

The project features high error correction to ensure scannability even with a logo overlay, custom brand colors, and automatic logo resizing.

---

## ✨ Key Features

- **High Error Correction:** Uses `ERROR_CORRECT_H` to ensure the QR remains functional even when a logo covers part of the data.
- **Brand Customization:** Supports custom foreground and background colors (Default: Fundación Kālida Corporate Orange).
- **Center Logo Overlay:** Automatically inserts and resizes a logo in the center of the QR code.
- **Smart Resizing:** The logo is automatically scaled to approximately **25%** of the QR size to maintain a balance between branding and readability.

---

## 🧱 Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - [`qrcode`](https://pypi.org/project/qrcode/) — Core QR code generation.
  - [`Pillow` (PIL)](https://pypi.org/project/Pillow/) — Image processing for logo resizing and composition.

---

## 🗂️ Project Structure

```text
python_app_QR/
├── crearqr.py                      # Main script (Primary logic)
├── crearqr2.py                     # Alternative version / Iteration
├── crearqr3.py                     # Alternative version / Iteration
├── 02-pictograma-calidez-Kalida.png # Corporate logo for overlay
├── LOGO_CA.jpg                     # Additional brand asset
├── LOGO_ES.jpg                     # Additional brand asset
└── QR_Kalida.png                   # Generated output (after execution)


⚙️ Configuration (Customizable)

The following parameters are configured within the scripts:

Parameter	Description	Current Value
URL	The destination link	https://www.fundaciokalida.org/es/
Brand Color	Corporate Foreground Color	RGB (245, 133, 110) / #F5856E
Logo Size	Relative size of the logo	25% of the QR area
Error Correction	Robustness level	ERROR_CORRECT_H (High)
🚀 Getting Started

1) Prerequisites
Python 3.x installed (on macOS you may need to use python3 / pip3)
2) Install dependencies



pip3 install qrcode[pil] Pillow
3) Run



python3 crearqr.py
The generated image (e.g., QR_Kalida.png) will appear in the project root directory.

🧭 Notes on Scannability

Contrast: Ensure the brand_color has enough contrast against the background for older camera sensors.
Logo Size: While the script defaults to 25%, increasing this value significantly may prevent some devices from scanning the code.
Assets: The script expects 02-pictograma-calidez-Kalida.png to be present in the same folder to perform the overlay.
📄 License & Usage

Copyright (c) 2024–2026 Jolman Gordillo. All Rights Reserved.

This repository is public exclusively for portfolio and technical code review purposes.

No permission is granted to copy, modify, redistribute, or use this code for commercial or personal projects.
Unauthorized use of the source code, assets, or design is strictly prohibited.
Developed by Jolman Gordillo
Website: https://jolmandeveloper.com
LinkedIn: https://www.linkedin.com/in/jolmang/