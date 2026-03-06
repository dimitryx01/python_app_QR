Descripción del Proyecto
Generador de códigos QR personalizados con logo central y colores corporativos. Creado específicamente para la Fundación Kālida.

Funcionalidades
Genera QR con alta corrección de errores (ERROR_CORRECT_H)
Personalización de colores (frente y fondo)
Inserción de logo en el centro del QR
Redimensionado automático del logo (25% del tamaño del QR)
Dependencias
pip install qrcode[pil] Pillow
Estructura de archivos necesaria
/
├── crearqr.py                           # Script principal
├── 02-pictograma-calidez-Kalida.png     # Logo a insertar
└── QR_Kalida.png                        # QR generado (output)

Configuración personalizable
Variable	Descripción	Valor actual
url	URL del QR	https://www.fundaciokalida.org/es/
brand_color	Color corporativo RGB	(245, 133, 110) #F5856E
logo_size	Tamaño del logo relativo al QR	25%
Uso: python crearqr.py

Tecnologías
Python 3
qrcode - Generación de códigos QR
Pillow (PIL) - Manipulación de imágenes
Notas
El script requiere un archivo de logo llamado 02-pictograma-calidez-Kalida.png
La alta corrección de errores permite que el QR sea escaneable incluso con el logo tapando parte del código