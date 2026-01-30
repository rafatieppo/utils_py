import pytesseract
from PIL import Image
import re

# You need to have Tesseract-OCR installed on your system for this to work.
# Also, install the required Python packages: pip install pytesseract Pillow

def extract_text_and_coordinates(image_path):
    """
    Extracts text from an image and attempts to find Latitude and Longitude coordinates.
    """
    try:
        # Open the image file
        img = Image.open(image_path)

        # Extract text using pytesseract
        extracted_text = pytesseract.image_to_string(img)

        print("--- Extracted Text ---")
        print(extracted_text)
        print("----------------------\n")

        # Define regex patterns to find latitude and longitude
        # This pattern looks for "Lat" or "Latitude" followed by a number (with optional negative sign and decimals)
        lat_pattern = re.compile(r'(Lat|Latitude).*?([-+]?\d*\.\d+|\d+)')
        # This pattern looks for "Long" or "Longitude" followed by a number (with optional negative sign and decimals)
        long_pattern = re.compile(r'(Long|Longitude).*?([-+]?\d*\.\d+|\d+)')

        latitude = None
        longitude = None

        # Search for the patterns in the extracted text
        lat_match = lat_pattern.search(extracted_text)
        if lat_match:
            # The coordinate value is in the second group of the match
            latitude = lat_match.group(2)

        long_match = long_pattern.search(extracted_text)
        if long_match:
            # The coordinate value is in the second group of the match
            longitude = long_match.group(2)

        # Print the results
        print("--- Found Coordinates ---")
        if latitude:
            print(f"Latitude: {latitude}")
        else:
            print("Latitude: Not found")
        
        if longitude:
            print(f"Longitude: {longitude}")
        else:
            print("Longitude: Not found")
        print("-------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_image.jpg' with the actual path to your image file.
# For the provided image, it would be something like:

image_file_path = './photo_2026-01-30_09-59-43.jpg' 

extract_text_and_coordinates(image_file_path)
