from django.forms import ModelForm
from . models import Employee, Timeline, Terms, Privacy

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

class PriacyForm(ModelForm):
    class Meta:
        model = Privacy
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PriacyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class TermsForm(ModelForm):
    class Meta:
        model = Terms
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TermsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})