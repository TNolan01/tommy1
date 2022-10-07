from django import forms
from django.forms import ModelForm
from .models import TextSlider, ContactUs

# Contact form for contact_us.html
# class ContactForm(forms.Form):
#     contact_name = forms.CharField()
#     email = forms.EmailField()
#     phone_number = forms.CharField(label='Phone')
#     message = forms.CharField(widget=forms.Textarea())


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
