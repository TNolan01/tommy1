from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('gallery', views.gallery, name='gallery'),
    path('SliderCreateView', views.SliderCreateView.as_view(), 
        name='slider_create_view'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]
