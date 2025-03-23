from django.contrib import admin
from App.models import Annotation,Image,Category, AnnotatedImage

# Register your models here.
admin.site.register(Annotation) 
admin.site.register(Image) 
admin.site.register(Category)
admin.site.register(AnnotatedImage)
