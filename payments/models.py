from django.db import models

# Create your models here.

from django.db import models

class PaymentProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) # Euros
    image = models.ImageField(upload_to='models/', null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_display_price(self):
        return "{0:.2f}".format(self.price)
    
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except: 
            url = ''
        return url
