from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'placeholder': 'Your name....'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email address....'}),
        required=True
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message....'}),
        required=True
    )
    captcha = CaptchaField(
                      error_messages={'invalid': 'Incorrect verification code'},
                      widget=CaptchaTextInput(attrs={'placeholder': 'Enter the letters listed above...'}),
                      required=True)
