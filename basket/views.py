from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Renders shopping basket


def view_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    product = product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request,
            f'Quantity for {product.product_name} updated to {basket[item_id]}.')
    else:
        basket[item_id] = quantity
        messages.success(
            request,
            f'{product.product_name} has been added to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


# Adjust quantity of a product in the basket
def adjust_basket(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.info(
            request,
            f'Quantity for {product.product_name} updated to {basket[item_id]}.')
    else:
        basket.pop[item_id]
        messages.info(
            request,
            f'Removed {product.product_name} from your basket.')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


# Remove a product from the basket
def remove_from_basket(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    try:
        basket.pop(item_id)
        messages.success(
            request,
            f'Removed {product.product_name} from your basket.')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error deleting item : {e}')
        return HttpResponse(status=500)
