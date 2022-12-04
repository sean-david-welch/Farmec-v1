from django.contrib import admin
from .models import Supplier, SipFact, MxFact, SulkyFact, Machine, Product

# Register your models here.
admin.site.register(Supplier)
admin.site.register(SipFact)
admin.site.register(MxFact)
admin.site.register(SulkyFact)
admin.site.register(Machine)
admin.site.register(Product)
