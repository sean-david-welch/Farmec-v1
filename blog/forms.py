from django.forms import ModelForm
from . models import Blog, Exhibition

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ExhibitionForm(ModelForm):
    class Meta:
        model = Exhibition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExhibitionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})