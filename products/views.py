from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Renders the all products page
def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None
    if request.GET:
        # filter to show products in their catergories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        #query for nav search function    
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"Please enter search query.")
                return redirect(reverse('products'))
            
            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            products = products.filter(queries)    
    
    context = {
        'products': products,
        'search_func': query,
        'product_cats': categories,
    }      
    
    return render(request, 'products/products.html', context)


# Renders the all product DETAIL page
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)    
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)