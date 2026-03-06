import qrcode
from PIL import Image, ImageDraw

# Enlace del QR
url = "https://www.fundaciokalida.org/es/"

# Generar QR con color corporativo
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(url)
qr.make(fit=True)

brand_color = (245, 133, 110)  # #F5856E

qr_img = qr.make_image(fill_color=brand_color, back_color="white").convert("RGBA")

# Abrir el logo
logo = Image.open("02-pictograma-calidez-Kalida.png").convert("RGBA")

# Redimensionar el logo
logo_size = int(qr_img.size[0] * 0.25)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calcular posición del logo
pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)

# Crear espacio en blanco para el logo (con padding alrededor)
draw = ImageDraw.Draw(qr_img)
padding = 10  # margen blanco alrededor del logo
x0, y0 = pos[0] - padding, pos[1] - padding
x1, y1 = pos[0] + logo_size + padding, pos[1] + logo_size + padding
draw.rectangle([x0, y0, x1, y1], fill="white")

# Pegar logo sobre el fondo blanco
qr_img.paste(logo, pos, mask=logo)

# Guardar imagen final
qr_img.save("QR_Kalida.png")

print("QR con logo limpio generado como QR_Kalida.png")