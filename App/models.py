from django.db import models

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Annotation(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bbox = models.JSONField()
    area = models.IntegerField()
    iscrowd = models.BooleanField(default=False)
 
 
class AnnotatedImage(models.Model):
    original_image = models.ImageField(upload_to='original_images/')
    annotated_image = models.ImageField(upload_to='annotated_images/')
    annotations = models.JSONField()  # Store annotations as JSON
    uploaded_at = models.DateTimeField(auto_now_add=True)
    ntn_number = models.CharField(max_length=50, blank=True, null=True)  # Add NTN field

    def __str__(self):
        return f"AnnotatedImage {self.id}"
