from django import forms
from django.forms import ModelForm
from .models import TextSlider, ContactUs

# Form to allow authenticated user update info in text carousel on index.html


class TextSliderForm(ModelForm):
    class Meta:
        model = TextSlider
        fields = '__all__'

        widgets = {
            'slider_info': forms.TextInput(attrs={'class': 'form-control'})
        }


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
