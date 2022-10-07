from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subscribed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
