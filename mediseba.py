import qrcode

# Base URL without hospital ID
base_url = "https://api.medi-sheba.referola.xyz/api/v1/hospitalId="

# Generate QR codes for hospital IDs from 2 to 30
for hospital_id in range(2, 31):
    url = f"{base_url}{hospital_id}"  # Construct the full URL
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=5,  # Adjust QR size
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as an image file with the hospital ID in the filename
    filename = f"qr_hospital_{hospital_id}.png"
    img.save(filename)

    print(f"QR Code generated for Hospital ID {hospital_id} and saved as '{filename}'.")
