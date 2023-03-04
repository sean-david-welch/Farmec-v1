from django.contrib import admin
from . models import SupplierPage, PartsPage, WarrantyClaim, MachineRegistration
from . models import PartsRequired

class PartsInline(admin.TabularInline):
    model = PartsRequired

class WarrantyAdmin(admin.ModelAdmin):
    inlines = [PartsInline]

# Register your models here.
admin.site.register(SupplierPage)
admin.site.register(PartsPage)
admin.site.register(WarrantyClaim, WarrantyAdmin)
admin.site.register(MachineRegistration)
