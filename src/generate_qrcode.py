import qrcode
import os

def generate_qr_code(url, file_path):
    """
    Generates a QR code from a URL and saves it as a PNG file.

    Parameters:
    url (str): The URL to encode in the QR code.
    file_path (str): The file path where the PNG file will be saved.
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image as a PNG file
    img.save(file_path)

def main():
    # Prompt the user for the URL
    url = input("Please enter the URL to encode in the QR code: ")
    
    # Prompt the user for the filename
    filename = input("Please enter the filename for the PNG file (will be saved in the images folder): ")

    # Ensure the images directory exists
    os.makedirs('images', exist_ok=True)

    # Generate QR code
    file_path = os.path.join('images', filename)
    generate_qr_code(url, file_path)

if __name__ == '__main__':
    main()