# Mobile Number Extractor

This is a web application for extracting mobile numbers from images. Users can upload multiple images, and the application will extract any mobile numbers found in the images and display them on the screen. The extracted mobile numbers are also saved in an Excel file.

## Table of Contents

- [Mobile Number Extractor](#mobile-number-extractor)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)

## Features

- Upload multiple images containing text.
- Extract mobile numbers from the uploaded images.
- Display extracted mobile numbers on the screen.
- Save extracted mobile numbers to an Excel file.
- Scrollable container for viewing extracted mobile numbers.

## Technologies

- Flask
- OpenCV
- Tesseract OCR
- PIL (Python Imaging Library)
- Pandas
- HTML
- CSS
- JavaScript

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Tesseract OCR (Download and install from [here](https://github.com/tesseract-ocr/tesseract))

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/SanyujaShelke/Number-Extractor-From-Image.git
    cd mobile-number-extractor
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv myvenv
    source myvenv/bin/activate   # On Windows, use `myvenv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set the path for Tesseract OCR in your `app.py` file:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # Adjust the path as needed
    ```

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Open the web application in your browser.
2. Click on the file input field and select one or more images.
3. Click the "Extract Mobile Numbers" button.
4. The extracted mobile numbers will be displayed on the screen.
5. The extracted mobile numbers will also be saved in an Excel file located at `data/mobile_numbers.xlsx`.