from django.shortcuts import render, redirect, reverse, HttpResponse

# Renders shopping basket

def view_basket(request):
    
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket',{})
    
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    
    request.session['basket'] = basket
    return redirect(redirect_url)


# Adjust quantity of a product in the basket
def adjust_basket(request, item_id):
    quantity = int(request.POST.get('quantity'))
    
    
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop[item_id]

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


# Remove a product from the basket
def remove_from_basket(request, item_id):
    basket = request.session.get('basket',{})
    try:
        basket.pop(item_id)
        
        request.session['basket'] = basket
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)