from django.contrib import admin
from .models import Supplier, Machine, Product

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Machine)
admin.site.register(Product)
