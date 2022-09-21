from django import forms
from .models import Customer, SalesEmail
from django.contrib import messages


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email',]

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if Customer.objects.filter(email=email).exists():
    #         raise forms.ValidationError('This email already exists.')
    #     return email

class SalesEmailForm(forms.ModelForm):
    class Meta:
        model = SalesEmail
        fields = '__all__'


class UnsubscribeForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email',]