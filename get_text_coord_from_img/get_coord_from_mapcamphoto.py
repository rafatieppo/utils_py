import json
import numpy as np
import cv2
import pathlib
import pytesseract
from PIL import Image
import re

# You need to have Tesseract-OCR installed on your system for this to work.
# Also, install the required Python packages: pip install pytesseract Pillow


def extract_text_and_coordinates(file_path):
    """
    Extracts text from an image and attempts to find Latitude and Longitude coordinates.
    """
    try:
        # Open the image file
        # 1. Load the image
        file_path = file_path
        img = cv2.imread(file_path)
        if img is None:
            print("Error: Could not load image.")
            return

        # 2. Upscale
        # Making the image larger helps separate letters that are close together.
        img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

        # 3. Convert to HSV (Hue, Saturation, Value)
        # This allows us to filter by "Brightness" rather than just color.
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # 4. Define "White"
        # White has very low Saturation (S) and very high Value (V).
        # These numbers define the range of white we want to keep.
        lower_white = np.array([0, 0, 160])   # Min brightness
        upper_white = np.array([179, 55, 255]) # Max brightness

        # 5. Create a Mask
        # Create bin img: White pixel become 255 white, everything else becomes 0 black.
        mask = cv2.inRange(hsv, lower_white, upper_white)

        # 6. Invert the image
        # Tesseract works best with BLACK text on a WHITE background.
        # Currently we have White text on Black background. Let's flip it.
        inverted_mask = cv2.bitwise_not(mask)

        # 7. Denoise (Optional)
        # Uses a small "kernel" to remove tiny white dots (noise) that aren't text.
        kernel = np.ones((2,2), np.uint8)
        processed_img = cv2.morphologyEx(inverted_mask, cv2.MORPH_OPEN, kernel)

        # 8. Extract Text
        # --psm 6: Assume a single uniform block of text.
        # lang='eng': If your text has Portuguese accents (ã, ê), change to lang='por'
        config = r'--oem 3 --psm 6'
        extracted_text = pytesseract.image_to_string(
            processed_img, config=config) #lang='eng')

        # Define regex patterns to find latitude and longitude
        # This pattern looks for "Lat" or "Latitude" followed by a number
        lat_pattern = re.compile(r'(Lat|Latitude|kat).*?([-+]?\d*\.\d+|\d+)')
        # This pattern looks for "Long" or "Longitude" followed by a number
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

        # Print extratec text
        # print("--- Extracted Text ---")
        # print(extracted_text)
        # print("----------------------\n")

        # Print the results
        print("--- Coordinates and path file---")
        if latitude or latitude:
            print(f"\nLatitude: {latitude}, \nLongitude: {longitude}, \
            \npathfile: {file_path}")

            data = {}
            data['lat'] = latitude
            data['lon'] = longitude
            try:
                fn = file_path.name
            except:
                fn = file_path
            data['file_path'] = fn
            print("--- json file coordinates ---")
            print(json.dumps(data, indent=4))
            return data
        else:
            print("Coordinates Not found")
        # Save the processed image so you can see what the computer sees
        # cv2.imwrite("debug_high_contrast.jpg", processed_img)

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_image.jpg' with the actual path to your image file.
# For the provided image, it would be something like:

# ------------------------------------------------------------
# how to use
# ------------------------------------------------------------


file_path = './nao_certo.jpg'
extract_text_and_coordinates(file_path)


lsimgs = pathlib.Path('./').glob('*.jpg')
for idx, f in enumerate(lsimgs):
    print('------------------------------------')
    print(f'{idx} -----> {f}')
    extract_text_and_coordinates(f)
    print('------------------------------------')
