from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
            
            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query) | Q(simple_description__icontains=query)
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
# Add a new product
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            form.save()
            messages.success(request,'Product added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,'Product not added, please check form')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

# Edit an existing product
def edit_product(request, product_id):
    product= get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Product details did not update, please check form')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Edit product : {product.product_name}')
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)

# Delete an existing product
def delete_product(request, product_id):
    product= get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted')
        # return redirect(reverse('products'))
        return redirect('products')
    return render(request, 'products/delete_product.html')

# Renders the special offers page
def special_offers(request):
    products = Product.objects.filter(special_offer=True)
    name = 'Special Offers'
    context = { 
        'products': products,
        'name': name,
    }

    return render(request, 'products/products.html', context)