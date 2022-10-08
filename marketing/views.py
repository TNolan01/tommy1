from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import CustomerForm, UnsubscribeForm
from .models import Customer
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.conf import settings


def marketing_signup(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if Customer.objects.filter(email=instance.email).exists():
            messages.info(request, 'Email is already on our newsletter list')
        else:
            instance.save()
            messages.success(request, 'Thank you for signing up!')
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'marketing/subscribe_email.html', context)


def marketing_unsubscribe(request):
    form = UnsubscribeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if Customer.objects.filter(email=instance.email).exists():
            Customer.objects.filter(email=instance.email).delete()
            messages.success(
                request, 'Email address has been deleted from newsletter')
            return redirect('/')
        else:
            messages.error(request, 'Email not found on our newsletter list')
    context = {
        'form': form,
    }
    return render(request, 'marketing/unsubscribe_email.html', context)


def newsletter(request):
    products = Product.objects.filter(special_offer=True)

    context = {
        'products': products,
    }
    return render(request, 'marketing/newsletter.html', context)


@login_required
def email_list(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers,
    }
    return render(request, 'marketing/email_list.html', context)

# Newsletter email sending function
# Code adapted from...
# https://docs.djangoproject.com/en/3.2/topics/email/#preventing-header-injection
# Bonsai Shop PP5 Project by Joanna Gorska https://github.com/JoGorska


@login_required
def send_newsletter(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owners can do that.')
        return redirect(reverse('/'))

    newsletter = Product.objects.filter(special_offer=True)
    customers = Customer.objects.all()

    for customer in customers:
        email = customer.email
        subject = render_to_string(
            'marketing/marketing_email/newsletter_email_subject.txt',
            {'newsletter': newsletter,
             'customers': customers})

        body = render_to_string(
            'marketing/marketing_email/newsletter_email_body.txt',
            {'newsletter': newsletter,
             'customers': customers,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        if subject and body and email:
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    messages.info(request,
                  f'Newsletter sent to {customers.count()}\
                       subscribers')
    return HttpResponseRedirect('/')


def remove_subscriber(request, customer_id):
    subscriber = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        subscriber.delete()
        messages.success(request, 'Subscriber deleted')
        return redirect('email_list')
    return render(request, 'marketing/remove_subscriber.html')
