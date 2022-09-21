from django.contrib import admin
from .models import Customer, SalesEmail

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email','subscribed_date',)

admin.site.register(Customer)
admin.site.register(SalesEmail)
