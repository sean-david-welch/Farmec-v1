from django.db import models
import uuid

# Create your models here.
class SupplierPage(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    logo_image = models.ImageField(null=True, blank=True, upload_to='models/', default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']

    @property
    def imageurl(self):
        try:
            url = self.logo_image.url
        except: 
            url = ''
        return url

class PartsPage(models.Model):
    supplier = models.ForeignKey(SupplierPage, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    catalogue_link = models.URLField(max_length=200, blank=True, null=True)
    supplier_page = models.URLField(max_length=200, blank=True, null=True)
    marketing_image = models.ImageField(null=True, blank=True, upload_to='models/', default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']

    @property
    def imageurl(self):
        try:
            url = self.marketing_image.url
        except: 
            url = ''
        return url

class WarrantyClaim(models.Model):
    dealer = models.CharField(max_length=200, blank=True, null=True)
    dealer_contact = models.CharField(max_length=200, blank=True, null=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    machine_model = models.CharField(max_length=200, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    install_date = models.CharField(max_length=200, blank=True, null=True)
    failure_date = models.CharField(max_length=200, blank=True, null=True)
    repair_date = models.CharField(max_length=200, blank=True, null=True)
    failure_details = models.TextField(blank=True, null=True)
    repair_details = models.TextField(blank=True, null=True)
    labour_hours = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        if self.owner_name and self.dealer:
            return str(self.owner_name + "-" + self.dealer)
        else:
            return str(self.id)

    class Meta:
        ordering = ['-created']

class PartsRequired(models.Model):
    warranty = models.ForeignKey(WarrantyClaim, on_delete=models.CASCADE, null=True, blank=True)
    part_number = models.CharField(max_length=200, blank=True, null=True)
    quantity_needed = models.CharField(max_length=20, blank=True, null=True, default=1)
    invoice_number = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

class MachineRegistration(models.Model):
    dealer_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Dealer Name")
    dealer_address = models.CharField(max_length=200, blank=True, null=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    owner_address = models.CharField(max_length=200, blank=True, null=True)
    machine_model = models.CharField(max_length=200, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    install_date = models.CharField(max_length=200, blank=True, null=True)
    invoice_number = models.CharField(max_length=200, blank=True, null=True)
    complete_supply = models.BooleanField(default=False, blank=True, null=True)
    pdi_complete = models.BooleanField(default=False, blank=True, null=True)
    pto_correct = models.BooleanField(default=False, blank=True, null=True)
    machine_test_run = models.BooleanField(default=False, blank=True, null=True)
    safety_induction = models.BooleanField(default=False, blank=True, null=True)
    operator_handbook = models.BooleanField(default=False, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True)
    completed_by = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.owner_name)

    class Meta:
        ordering = ['-created']
    

