import os
import json
import django
from django.conf import settings

# Initialize Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InvoiceProject.settings')  # Replace 'your_project' with your project name
django.setup()

# Import models after initializing Django
from App.models import Image, Category, Annotation  # Replace 'App' with the actual app name

# Function to populate the database
def populate_database():
    folder_path = "output_jsons"
    files = sorted(os.listdir(folder_path))[:20]  # Only process the first 20 files

    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r') as f:
            data = json.load(f)

            # Save Images
            for img in data.get("images", []):
                image_obj, created = Image.objects.get_or_create(
                    id=img["id"],
                    defaults={"file_name": img["file_name"], "width": img["width"], "height": img["height"]}
                )

            # Save Categories
            for cat in data.get("categories", []):
                Category.objects.get_or_create(id=cat["id"], defaults={"name": cat["name"]})

            # Save Annotations
            for ann in data.get("annotations", []):
                Annotation.objects.create(
                    image_id=ann["image_id"],
                    category_id=ann["category_id"],
                    bbox=ann["bbox"],
                    area=ann["area"],
                    iscrowd=ann["iscrowd"]
                )



    print("Processed and saved data from 20 files.")

if __name__ == "__main__":
    populate_database()


