from django.shortcuts import render, redirect
from marketing.forms import CustomerForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


# Renders home page
def index(request):
    
    return render(request, 'home/index.html')


# Renders contact us page
def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data["contact_name"]
            from_email = form.cleaned_data["email"]
            phone_number = form.cleaned_data['phone_number']
            subject = contact_name + ' ' + phone_number
            message = form.cleaned_data['message']
            recipient_list = ['sales@thissite.com']
            try:
                # send_mail(contact_name, email, phone_number, message, ['sales@site.ie'])
                send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request,'We will be in contact with you shortly')
            return redirect('/')
    return render(request, 'home/contact_us.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up!') 
            return redirect('/')
    else:
        form = CustomerForm()
    context = {'form': form}

    return render(request, 'home/subscribe_email.html', context)


# Renders gallery - inspiration page
def gallery(request):
    
    return render(request, 'home/gallery.html')