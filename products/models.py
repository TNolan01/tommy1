from django.db import models

# Models relating to the products

class Category(models.Model):
        class Meta:
            verbose_name_plural = 'Categories'
    
        name = models.CharField(max_length=100)
        trade_name = models.CharField(max_length=100, null=True, blank=True)
        
        def __str__(self):
            return self.name

        def get_trade_name(self):
            return self.trade_name


class ProductMeasurement(models.Model):
    sell_quantity = models.CharField(max_length=100)
    
    def __str__(self):
        return self.sell_quantity
    
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    simple_description = models.TextField(default=None, null=True, blank=True)
    product_description = models.TextField()
    sell_quantity = models.ForeignKey('ProductMeasurement', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    star_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    special_offer = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.product_name