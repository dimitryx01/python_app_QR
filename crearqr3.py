import qrcode
from PIL import Image, ImageDraw

# Enlace destino del QR
url = "https://www.fundaciokalida.org/es/"

# Crear objeto QR con alta corrección de error (permite tapar parte del código con logo)
qr = qrcode.QRCode(
    version=4,  # tamaño del QR (puedes subir a 5-10 si quieres más resolución)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,  # tamaño de cada punto
    border=2,     # margen externo
)
qr.add_data(url)
qr.make(fit=True)

# Colores de marca
brand_color = (245, 133, 110)  # #F5856E
background_color = (255, 255, 255)  # blanco

# Imagen base en color corporativo
qr_img = qr.make_image(fill_color=brand_color, back_color=background_color).convert("RGBA")

# --- Opcional: redondear los "píxeles" del QR para estilo moderno
# Redibujo el QR pixel a pixel en círculos
w, h = qr_img.size
pixels = qr_img.load()
circle_qr = Image.new("RGBA", qr_img.size, background_color)
draw = ImageDraw.Draw(circle_qr)

radius = qr.box_size // 2
for y in range(0, h, qr.box_size):
    for x in range(0, w, qr.box_size):
        if pixels[x, y][0:3] == brand_color:  # si es del color del QR
            draw.ellipse(
                (x, y, x + qr.box_size, y + qr.box_size),
                fill=brand_color
            )

qr_img = circle_qr

# --- Insertar logo en el centro ---
logo = Image.open("LOGO_ES.jpg").convert("RGBA")

# Redimensiono logo (20-25% del tamaño del QR)
logo_size = int(qr_img.size[0] * 0.25)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Pongo un fondo blanco detrás del logo (como Starbucks)
pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
draw.rectangle(
    [pos[0]-15, pos[1]-15, pos[0]+logo_size+15, pos[1]+logo_size+15],
    fill=background_color
)

# Pegar logo sobre el centro
qr_img.paste(logo, pos, mask=logo)

# Guardar archivo
qr_img.save("QR_Kalida_Brand.png")

print("✅ QR estilizado generado como 'QR_Kalida_Brand.png'")