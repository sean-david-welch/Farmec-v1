from django.db import models

# Create your models here.
# from django.db import models

# Create your models here.
class StripeProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(default=0, null=True, blank=True) #cents
    file = models.FileField(upload_to="product_files/", null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False, null=False)

    def __str__(self):
        return str(self.name)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    class Meta:
        ordering = ['created']

class PaymentProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(default=0, null=True, blank=True) #cents
    file = models.FileField(upload_to="product_files/", null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    
