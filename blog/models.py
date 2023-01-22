from django.db import models
import uuid

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True) 
    main_image = models.ImageField(null=True, blank=True, upload_to='models/', default="default.jpg")
    subheading = models.CharField(max_length=200, blank=True, null=True) 
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']

    @property
    def imageurl(self):
        try:
            url = self.main_image.url
        except: 
            url = ''
        return url

class Exhibition(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['created'] 




