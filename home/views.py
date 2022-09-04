from django.shortcuts import render
from marketing.forms import CustomerForm
from django.contrib import messages
from django.conf import settings


# Renders home page
def index(request):
    
    return render(request, 'home/index.html')

# Renders contact us page
def contact_us(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to our newsletter.')
            return redirect('contact_us/')
    else:
        form = CustomerForm()
    context = {'form': form}

    return render(request, 'home/contact_us.html')