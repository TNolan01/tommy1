from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from .forms import ContactUsForm, TextSliderForm
from .models import TextSlider

from django.urls import reverse_lazy

# Renders home page


def index(request):
    slider = TextSlider.objects.filter()[0]
    context = {
        'slider': slider
    }
    return render(request, 'home/index.html', context)


# Contact Us Form with email send function
def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            email_message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            subject = f'New sales contact {form.cleaned_data["email"]}: {form.cleaned_data["contact_name"]}'
            body = form.cleaned_data['message']
            if subject and body and email:
                try:
                    send_mail(
                        subject,
                        body,
                        settings.DEFAULT_FROM_EMAIL,
                        [settings.DEFAULT_FROM_EMAIL],
                    )
                    messages.success(
                        request, 'We will be in contact with you shortly')
                    return redirect('home')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                return HttpResponse(
                    'Make sure all fields are entered and valid.')
    form = ContactUsForm()
    context = {'form': form}
    return render(request, 'home/contact_us.html', {'form': form})


# Renders gallery - inspiration page
def gallery(request):

    return render(request, 'home/gallery.html')


# Class view for updating index.html text slider
class SliderCreateView(LoginRequiredMixin, UpdateView):
    model = TextSlider
    form_class = TextSliderForm
    template_name = 'home/slider_form.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = TextSlider.objects.filter()[0]
        return obj


# Render the Privacy Policy page
def privacy_policy(request):

    return render(request, 'home/privacy_policy.html')
