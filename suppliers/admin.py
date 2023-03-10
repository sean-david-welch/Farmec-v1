from django.contrib import admin
from .models import Supplier, Machine, Product, Video

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Machine)
admin.site.register(Product)
admin.site.register(Video)
