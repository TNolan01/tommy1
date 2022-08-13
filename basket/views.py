from django.shortcuts import render

# Renders shopping basket

def view_basket(request):
    
    return render(request, 'basket/basket.html')

