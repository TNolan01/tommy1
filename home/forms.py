from django import forms

#Contact form for contact_us.html

class ContactForm(forms.Form):
    contact_name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(label='Phone')
    message = forms.CharField(widget=forms.Textarea())