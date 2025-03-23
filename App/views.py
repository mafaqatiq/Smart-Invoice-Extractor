from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from ultralytics import YOLO
import pytesseract
import cv2
import os

# Label mapping for tensor values
label_mapping = {
    0: "company_dealing_in_value",
    1: "Supplier_NTN_label",
    2: "Supplier_NTN_value",
    3: "Supplier_Name_label",
    4: "Supplier_Name_value",
    5: "Supplier_S_T_Reg_No_label",
    6: "Supplier_S_T_Reg_No_value",
    7: "Supplier_Address_label",
    8: "Supplier_Address_value",
    9: "Supplier_Phone_Number_label",
    10: "Supplier_Phone_Number_value",
    11: "Buyer_NTN_label",
    12: "Buyer_NTN_value",
    13: "Buyer_Name_label",
    14: "Buyer_Name_value",
    15: "Buyer_S_T_Reg_No_label",
    16: "Buyer_S_T_Reg_No_value",
    17: "Buyer_Address_label",
    18: "Buyer_Address_value",
    19: "Products_Description_label",
    20: "Products_1_Description_value",
    21: "Products_2_Description_value",
    22: "Products_3_Description_value",
    23: "Products_4_Description_value",
    24: "Products_Quantity_label",
    25: "Products_1_Quantity_value",
    26: "Products_2_Quantity_value",
    27: "Products_3_Quantity_value",
    28: "Products_4_Quantity_value",
    29: "Products_Rate_label",
    30: "Products_1_Rate_value",
    31: "Products_2_Rate_value",
    32: "Products_3_Rate_value",
    33: "Products_4_Rate_value",
    34: "Products_Amount_Excluding_Tax_label",
    35: "Products_1_Amount_Excluding_Tax_value",
    36: "Products_2_Amount_Excluding_Tax_value",
    37: "Products_3_Amount_Excluding_Tax_value",
    38: "Products_4_Amount_Excluding_Tax_value",
    39: "Products_Sales_Tax_At_18%_Tax_label",
    40: "Products_1_Sales_Tax_At_18%_Tax_value",
    41: "Products_2_Sales_Tax_At_18%_Tax_value",
    42: "Products_3_Sales_Tax_At_18%_Tax_value",
    43: "Products_4_Sales_Tax_At_18%_Tax_value",
    44: "Products_Amount_Including_Tax_label",
    45: "Products_1_Amount_Including_Tax_value",
    46: "Products_2_Amount_Including_Tax_value",
    47: "Products_3_Amount_Including_Tax_value",
    48: "Products_4_Amount_Including_Tax_value",
    49: "Products_Total_Amount_Excluding_Tax_label",
    50: "Products_Total_Amount_Excluding_Tax_value",
    51: "Products_Total_Sales_Tax_At_18%_Amount_label",
    52: "Products_Total_Sales_Tax_At_18%_Amount_value",
    53: "Products_Total_Amount_Including_Tax_label",
    54: "Products_Total_Amount_Including_Tax_value",
    55: "Date_label",
    56: "Date_value"
}

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
model = YOLO(r'App/Best_model_1.pt')  # Replace with your trained YOLO model path


def home(request):
    return render(request, 'firstApp/home.html')
 
from django.shortcuts import render
from django.conf import settings
from .models import AnnotatedImage
import os
import cv2
import pytesseract

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        if uploaded_file:
            # Save the uploaded file temporarily
            temp_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            with open(temp_path, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            try:
                # Process the image
                image = cv2.imread(temp_path)
                results = model.predict(temp_path, conf=0.26)
                extracted_data = []
                ntn_value = None  # This will store the NTN value

                for result in results:
                    for box in result.boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cropped_region = image[y1:y2, x1:x2]
                        text = pytesseract.image_to_string(cropped_region).strip()
                        label = int(box.cls.item())  # Convert the tensor value to an integer
                        
                        # Add the corresponding label name using the label_mapping dictionary
                        label_name = label_mapping.get(label, "Unknown")
                        
                        # If the label is 'Supplier_NTN_value', store the text in ntn_value
                        if label_name == "Supplier_NTN_value":
                            ntn_value = text  # Save the extracted NTN value
                        
                        extracted_data.append({
                            'label': label_name,
                            'text': text,
                            'coords': (x1, y1, x2, y2),
                        })
                        # Annotate image
                        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Save the annotated image
                annotated_image_path = os.path.join(settings.MEDIA_ROOT, 'annotated_' + uploaded_file.name)
                cv2.imwrite(annotated_image_path, image)

                # Save the data to the database
                annotated_image_instance = AnnotatedImage.objects.create(
                    original_image=uploaded_file,
                    annotated_image='annotated_' + uploaded_file.name,
                    annotations=extracted_data,
                    ntn_number=ntn_value  # Save the extracted NTN number here
                )

                # Construct annotated image URL
                annotated_image_url = settings.MEDIA_URL + 'annotated_' + uploaded_file.name
                
                # Render the response
                return render(request, 'firstApp/upload.html', {
                    'data': extracted_data,
                    'annotated_image_url': annotated_image_url,
                })
            finally:
                # Remove the temporary file if it exists
                if os.path.exists(temp_path):
                    os.remove(temp_path)

    return render(request, 'firstApp/upload.html')


from django.shortcuts import render
from .models import Image, Category, Annotation

def show_data(request):
    # Retrieve all records from the database
    images = Image.objects.all()
    categories = Category.objects.all()
    annotations = Annotation.objects.all()

    # Pass data to template
    return render(request, 'firstApp/show_data.html', {
        'images': images,
        'categories': categories,
        'annotations': annotations
    })

def show_extracted_data(request):
    # Retrieve all annotated images and their data
    annotated_images = AnnotatedImage.objects.all()

    return render(request, 'firstApp/show_extracted_data.html', {
        'annotated_images': annotated_images,
    })



from django.shortcuts import render
from App.models import AnnotatedImage
from App.forms import NTNSearchForm

def search_ntn(request):
    form = NTNSearchForm()
    search_results = None

    if request.method == "POST":
        form = NTNSearchForm(request.POST)
        if form.is_valid():
            ntn_number = form.cleaned_data['ntn_number']
            # Search for AnnotatedImage where the NTN number matches
            search_results = AnnotatedImage.objects.filter(ntn_number=ntn_number)

    return render(request, 'firstApp/search_ntn.html', {
        'form': form,
        'search_results': search_results
    })
