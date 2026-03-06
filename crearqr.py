import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image

# Enlace del QR
url = "https://www.fundaciokalida.org/es/"

# Generar QR base
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(url)
qr.make(fit=True)

# Color corporativo Kālida (extraído del pictograma adjunto)
brand_color = (245, 133, 110)  # hex #F5856E

# Crear QR con color corporativo y fondo blanco
qr_img = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=brand_color)
).convert("RGBA")

# Insertar logo en el centro
logo = Image.open("02-pictograma-calidez-Kalida.png").convert("RGBA")

# Redimensionar logo para que no tape demasiado el QR
logo_size = int(qr_img.size[0] * 0.25)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo)

# Guardar QR final
qr_img.save("QR_Kalida.png")

"QR_Kalida.png creado correctamente"