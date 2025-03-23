<<<<<<< HEAD
# Smart-Invoice-Extraction-System
=======
# Django Invoice Data Extraction Web App

This Django web application allows users to upload invoices, which are then processed using a YOLO model and Tesseract OCR. The app extracts annotated images and text data from the invoices, allowing users to search for specific information (e.g., by `supplier_ntn_value`) and view all extracted data stored in the database.

## Features
- **Invoice Upload**: Users can upload invoices in image format (e.g., PNG, JPG).
- **YOLO Model for Annotation**: The application uses the YOLO model to detect and annotate relevant parts of the invoice.
- **OCR Text Extraction**: Tesseract OCR is used to extract text from the invoice.
- **Database Storage**: All extracted data is stored in the database.
- **Search Functionality**: Users can search the extracted data by `supplier_ntn_value`.
- **View Data**: Display all stored invoice data from the database.

## Requirements
- Python 
- Django 
- Ultralytics (for YOLO model)
- CV2
- Tesseract OCR 

 
# Steps
## Configure Tesseract OCR
Install Tesseract OCR on your system if it's not already installed:

Windows: Download and install from here.
Make sure Tesseract is added to your system’s PATH variable.


## Run the server
python manage.py runserver




>>>>>>> df7f3d9 (code)
