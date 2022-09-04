from django import forms
from .models import Customer, SalesEmail


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class SalesEmailForm(forms.ModelForm):
    class Meta:
        model = SalesEmail
        fields = '__all__'
        