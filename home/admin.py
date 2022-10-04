from django.contrib import admin
from .models import TextSlider, ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact_name',
        'email',
        'contact_number',
    )

admin.site.register(TextSlider)
admin.site.register(ContactUs, ContactAdmin)

