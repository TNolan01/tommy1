from django.db import models

class TextSlider(models.Model):
    slider_header = models.CharField(max_length=20, null=True, default='Shop Online')
    slider_info = models.TextField(max_length=120, null=True,)

    def __str__(self):
        return self.slider_header
