from django.db.models.base import Model
from django import forms
from django.forms import ModelForm, widgets, forms, formsets
from . models import WarrantyClaim, MachineRegistration, SupplierPage, PartsPage
from . models import PartsRequired

class WarrantyClaimForm(ModelForm):
    class Meta:
        model = WarrantyClaim
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WarrantyClaimForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class PartsRequiredForm(ModelForm):
    class Meta:
        model = PartsRequired
        # fields = '__all__'
        exclude = ['warranty', 'id']

    def __init__(self, *args, **kwargs):
        super(PartsRequiredForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SupplierPageForm(ModelForm):
    class Meta:
        model = SupplierPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SupplierPageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class PartsPageForm(ModelForm):
    class Meta:
        model = PartsPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartsPageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class MachineRegistrationForm(ModelForm):
    class Meta:
        model = MachineRegistration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MachineRegistrationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


    