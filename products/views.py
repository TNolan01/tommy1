from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # For search function
from django.db.models.functions import Lower # For product sort via name
from .models import Product, Category
from .forms import ProductForm

# Renders the all products page
def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        # product sorting function
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'product_name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('product_name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
            
        # filter to show products in their catergories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
            
        # query for nav search function    
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"Please enter search query.")
                return redirect(reverse('products'))
            
            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            products = products.filter(queries)    
    
    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_func': query,
        'product_cats': categories,
        'current_sorting': current_sorting,
    }      
    
    return render(request, 'products/products.html', context)


# Renders the product DETAIL page
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)    
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)

# Product admin search
def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)