from django.db import models

# Create your models here.

class PaymentProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(default=0, null=True, blank=True) #cents
    image = models.ImageField(upload_to='models/', null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except: 
            url = ''
        return url
