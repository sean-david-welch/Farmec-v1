from django.db import models
import uuid

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    logo_image = models.ImageField(null=True, blank=True, upload_to='models/', default="models/default.jpg")
    description = models.TextField(blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    product_image = models.ImageField(null=True, blank=True, upload_to='models/', default="models/default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)
