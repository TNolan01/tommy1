from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from .forms import CustomerForm, SalesEmailForm

def marketing_signup(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if Customer.objects.filter(email=instance.email).exists():
             messages.info(request, 'Email is already on our newsletter list')
        else:
            instance.save()
    context = {
        'form': form,
    }
    return render(request, 'marketing/subscribe_email.html', context)

def marketing_unsubscribe(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if Customer.objects.filter(email=instance.email).exists():
            Customer.objects.filter(email=instance.email).delete()
            messages.success(request, 'Email address has been deleted from newsletter')
        else:
            messages.error(request, 'Email not found on our newsletter list')
    context = {
        'form': form,
    }
    return render(request, 'marketing/unsubscribe_email.html', context)
    