from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from . models import PaymentProduct

class PaymentProductForm(ModelForm):
    class Meta:
        model = PaymentProduct
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PaymentProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})