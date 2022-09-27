from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_type': 'Customer Type',          
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
            'default_phone_number': 'Phone Number',
        }
        self.fields['customer_type'].label = "Customer Type"
        self.fields['default_town_or_city'].label = "Town or City"
        self.fields['default_street_address1'].label = "Address 1"
        self.fields['default_street_address2'].label = "Address 2"
        self.fields['default_county'].label = "County"
        self.fields['default_postcode'].label = "Postal Code"
        self.fields['default_phone_number'].label = "Phone Number"