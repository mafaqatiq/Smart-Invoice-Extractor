# Smart-Invoice-Extraction-System

## Django Invoice Data Extraction Web App

This Django web application allows users to upload invoices, which are then processed using a YOLO model and Tesseract OCR. The app extracts annotated images and text data from the invoices, allowing users to search for specific information (e.g., by `supplier_ntn_value`) and view all extracted data stored in the database.

## Features

✅ **Invoice Upload**: Users can upload invoices in image format (e.g., PNG, JPG).  
✅ **YOLO Model for Annotation**: The application uses the YOLO model to detect and annotate relevant parts of the invoice.  
✅ **OCR Text Extraction**: Tesseract OCR is used to extract text from the invoice.  
✅ **Database Storage**: All extracted data is stored in a database for easy retrieval.  
✅ **Search Functionality**: Users can search the extracted data by `supplier_ntn_value`.  
✅ **View Data**: Displays all stored invoice data in an organized format.  

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mafaqatiq/Smart-Invoice-Extractor.git
cd Smart-Invoice-Extractor
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Tesseract OCR
- Install Tesseract OCR on your system:
  - **Windows**: Download from [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) and add it to the system PATH.
  - **Linux/macOS**: Install via package manager:
    ```bash
    sudo apt install tesseract-ocr  # Ubuntu/Debian
    brew install tesseract           # macOS
    ```

### 5️⃣ Run Database Migrations
```bash
python manage.py migrate
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```
Access the application at: **http://127.0.0.1:8000/**

---

## Usage
1. **Upload an Invoice**: Navigate to the upload page and select an invoice image.
2. **Processing**: The YOLO model detects relevant sections, and Tesseract OCR extracts text.
3. **Search Extracted Data**: Use the search function to find specific data (e.g., `supplier_ntn_value`).
4. **View All Data**: Browse all stored invoice data from the database.

---

## Technologies Used
- **Django** - Web framework for building the app
- **YOLO (Ultralytics)** - Object detection model for invoice annotation
- **Tesseract OCR** - Optical character recognition for extracting text
- **OpenCV (cv2)** - Image processing
- **SQLite** - Database for storing extracted data

---

## Contributing
Feel free to submit issues or pull requests to improve this project!

### 📧 Contact
For queries, contact: [mafaqatiq@gmail.com]

---
 
