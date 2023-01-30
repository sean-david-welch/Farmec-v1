from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']


class Stat(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.FileField(upload_to='models/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['svg'])])
    subheading = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['created']

    @property
    def imageurl(self):
        try:
            url = self.image.url
        except: 
            url = ''
        return url

class Special(models.Model):
    image = models.FileField(upload_to='models/', blank=True, null=True, default="default.jpg", validators=[FileExtensionValidator(allowed_extensions=['svg'])])
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

    def anchor(self, *args, **kwargs):
        self.link = reverse(self.link)
        super().anchor(*args, **kwargs)

    class Meta:
        ordering = ['created']

    @property
    def imageurl(self):
        try:
            url = self.image.url
        except: 
            url = ''
        return url