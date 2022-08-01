from django.shortcuts import render
from .models import Product

# Renders the all products page
def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
