from django.contrib import admin
from . models import StripeProduct, PaymentProduct

# Register your models here.
admin.site.register(StripeProduct)
admin.site.register(PaymentProduct)