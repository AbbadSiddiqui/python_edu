import qrcode
from PIL import Image  # Import Image from Pillow

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#6aff9b")
    img.save(file_name)
    print(f"QR Code saved as {file_name}")
    img.show()  # Display the QR code in a window

def display_qr_in_terminal(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr.print_ascii()  # Display the QR code in the terminal as ASCII art

if __name__ == "__main__":
    print("Welcome to the QR Code Generator!")
    text = input("Enter the text or URL to encode in the QR code: ")
    file_name = input("Enter the file name to save the QR code (e.g., qr_code.png): ")

    # Generate and display the QR code
    generate_qr_code(text, file_name)

    # Optionally display the QR code in the terminal
    print("\nQR Code displayed in the terminal:")
    display_qr_in_terminal(text)