from flask import Flask, request, render_template, jsonify
import cv2
import pytesseract
import re
from PIL import Image
import os
import pandas as pd
import logging

app = Flask(__name__)

# Set the path for tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Ensure the uploads and data directories exist
os.makedirs('uploads', exist_ok=True)
os.makedirs('data', exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_mobile_numbers', methods=['POST'])
def extract_mobile_numbers():
    if 'images' not in request.files:
        return jsonify({'error': 'No images uploaded'}), 400
    
    images = request.files.getlist('images')

    extracted_numbers = []

    for image in images:
        image_path = os.path.join('uploads', image.filename)
        image.save(image_path)

        # Extract text from the image
        extracted_text = extract_text_from_image(image_path)

        # Extract mobile numbers from the text
        mobile_numbers = extract_mobile_numbers_from_text(extracted_text)

        # Append extracted numbers to the list
        extracted_numbers.extend(mobile_numbers)

    # Save mobile numbers to an Excel file
    save_to_excel(extracted_numbers)

    return jsonify({'mobile_numbers': extracted_numbers})

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pil_image = Image.fromarray(gray)
    text = pytesseract.image_to_string(pil_image)
    logging.debug(f"Extracted Text: {text}")
    return text

def extract_mobile_numbers_from_text(text):
    mobile_number_pattern = r"\+91 \d{5} \d{5}|\+91\d{10}|\d{10}|\+91 \d{3} \d{3} \d{4}"
    mobile_numbers = re.findall(mobile_number_pattern, text)
    logging.debug(f"Extracted Mobile Numbers: {mobile_numbers}")
    return mobile_numbers

def save_to_excel(mobile_numbers, file_path="data/mobile_numbers.xlsx"):
    # Ensure the file_path directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Check if the file already exists
    if os.path.exists(file_path):
        # Load the existing data
        existing_df = pd.read_excel(file_path)
        logging.debug(f"Existing DataFrame loaded with {len(existing_df)} rows")
    else:
        # Create an empty DataFrame if the file does not exist
        existing_df = pd.DataFrame(columns=["Mobile Numbers"])
        logging.debug("No existing DataFrame found, creating a new one")

    # Create a new DataFrame for the new mobile numbers
    new_df = pd.DataFrame(mobile_numbers, columns=["Mobile Numbers"])
    logging.debug(f"New DataFrame created with {len(new_df)} rows")

    # Append the new data to the existing data
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    logging.debug(f"Combined DataFrame created with {len(combined_df)} rows")
    
    # Save the combined DataFrame to the Excel file
    combined_df.to_excel(file_path, index=False)
    logging.debug(f"DataFrame saved to {file_path}")

if __name__ == '__main__':
    app.run(debug=True)
