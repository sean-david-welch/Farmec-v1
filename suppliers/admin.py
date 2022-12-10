from django.contrib import admin
from .models import Supplier, Fact, Machine, Product

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Fact)
admin.site.register(Machine)
admin.site.register(Product)

