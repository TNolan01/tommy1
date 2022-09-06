from django.shortcuts import render, redirect
from marketing.forms import CustomerForm
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


# Renders home page
def index(request):
    
    return render(request, 'home/index.html')

# Renders contact us page
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We will be in contact with you shortly') 
            return redirect('/')
    else:
        form = ContactForm()
    context = {'form': form}

    return render(request, 'home/contact_us.html', context)


def subscribe(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We will be in contact with you shortly') 
            return redirect('/')
    else:
        form = CustomerForm()
    context = {'form': form}

    return render(request, 'home/subscribe_email.html', context)

