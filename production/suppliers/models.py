from django.db import models
import uuid

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    logo_image = models.ImageField(null=True, blank=True, upload_to='models/', default="default.jpg")
    marketing_image = models.ImageField(null=True, blank=True, upload_to='models/', default="default.jpg")
    description = models.TextField(blank=True, null=True)
    facts = models.TextField(blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']

    @property
    def imageurl(self):
        try:
            url = self.logo_image.url
        except: 
            url = ''
        return url

    @property
    def marketing_imageurl(self):
        try:
            url = self.marketing_image.url
        except: 
            url = ''
        return url
    
class Video(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    web_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    video_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['created']

class Machine(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    machine_image = models.ImageField(null=True, blank=True, upload_to='models/', default="default.jpg")
    description = models.TextField(blank=True, null=True)
    machine_link = models.URLField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return str(self.name)

    @property
    def imageurl(self):
        try:
            url = self.machine_image.url
        except: 
            url = ''
        return url

class Product(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    product_image = models.ImageField(null=True, blank=True, upload_to='models/', default="default.jpg")
    description = models.TextField(blank=True, null=True)
    product_link = models.URLField(max_length=200, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.name)

    @property
    def imageurl(self):
        try:
            url = self.product_image.url
        except: 
            url = ''
        return url