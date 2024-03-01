from django.db import models

# Create your models here.

class PaymentProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    serialnumber = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8, null=True, blank=True)
    image = models.ImageField(upload_to='models/', null=True, blank=True)

    def get_price_in_cents(self):
        return int(self.price * 100)  # Convert Decimal to integer

    def get_price_in_euros(self):
        return self.price  # Return the Decimal value

    def __str__(self):
        return str(self.name)
    
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except: 
            url = ''
        return url