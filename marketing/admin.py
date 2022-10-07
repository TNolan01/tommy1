from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribed_date',)


admin.site.register(Customer)
