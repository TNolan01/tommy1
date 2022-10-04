from django.db import models

class TextSlider(models.Model):
    slider_header = models.CharField(max_length=20, null=True, default='Shop Online')
    slider_info = models.TextField(max_length=120, null=True,)

    def __str__(self):
        return self.slider_header


class ContactUs(models.Model):
    contact_name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name_plural = "contact us"



