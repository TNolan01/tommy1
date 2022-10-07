from django.contrib import admin
from .models import Product, Category, ProductMeasurement


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'product_name',
        'product_description',
        'sell_quantity',
        'price',
        'star_rating',
        'special_offer',
        'image_url',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'trade_name',
    )


class ProductMeasurementAdmin(admin.ModelAdmin):
    list_display = (
        'sell_quantity',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductMeasurement, ProductMeasurementAdmin)
