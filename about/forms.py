from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from . models import Employee, Timeline

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class TimelineForm(ModelForm):
    class Meta:
        model = Timeline
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TimelineForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})