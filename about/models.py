from django.db import models
import uuid
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    role = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='models/', default="models/default.jpg")
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_whatsapp = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                            primary_key=True, editable=False,)
                            
    class Meta:
        ordering = ['created']

    @property
    def imageurl(self):
        try:
            url = self.profile_image.url
        except: 
            url = ''
        return url