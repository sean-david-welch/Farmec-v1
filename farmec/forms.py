from django import forms
import os
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

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
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(),
        public_key= os.environ.get('RECAPTCHA_PUBLIC_KEY'),
        private_key = os.environ.get('RECAPTCHA_PRIVATE_KEY'),
                            )
