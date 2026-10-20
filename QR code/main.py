import qrcode
import cv2

def encode_text_to_qr():
    # Text to encode in the QR code
    data = input("Enter the text to encode into QR code: ")

    # Generate QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    filename = input("Enter the filename to save the QR code image (e.g., qr_code.png): ")
    qr_image.save(filename)
    print(f"QR code generated and saved as '{filename}'")

def decode_qr_from_image():
    # Read the image containing the QR code
    image_path = input("Enter the path to the image containing the QR code: ")
    image = cv2.imread(image_path)

    # Initialize the QRCode detector
    qr_detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    data, bbox, _ = qr_detector.detectAndDecode(image)

    if bbox is not None:
        print(f"QR Code detected with data: {data}")
    else:
        print("QR Code not detected or could not be decoded.")

def main():
    while True:
        print("\n*** QR Code Encoder/Decoder ***")
        print("1. Encode text to QR code")
        print("2. Decode QR code from an image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            encode_text_to_qr()
        elif choice == '2':
            decode_qr_from_image()
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
