from django import forms

class ContactForm(forms.Form):
    name =  forms.CharField(max_length=250)
    email =  forms.EmailField()
    body =  forms.CharField(widget=forms.Textarea)