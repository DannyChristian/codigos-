import qrcode

# URL de tu aplicación de Streamlit
streamlit_url = 'http://localhost:8501/'

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(streamlit_url)
qr.make(fit=True)

# Crear una imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen del QR en un archivo
img.save("streamlit_qr_code.png")

print("Código QR generado y guardado como streamlit_qr_code.png")
