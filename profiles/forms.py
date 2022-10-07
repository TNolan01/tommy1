from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_type'].label = "Customer Type"
        self.fields['default_town_or_city'].label = "Town or City"
        self.fields['default_street_address1'].label = "Address 1"
        self.fields['default_street_address2'].label = "Address 2"
        self.fields['default_county'].label = "County"
        self.fields['default_postcode'].label = "Postal Code"
        self.fields['default_phone_number'].label = "Phone Number"
