import qrcode

# URL to encode in the QR code
url = "https://play.google.com/store/apps/details?id=com.banglartrainuserapp.app"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 = smallest, 40 = largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border width (minimum is 4)
)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qr_code.png")

print("QR Code generated and saved as 'qr_code.png'.")
