from django.urls import path 
from . import views

urlpatterns = [
    path('marketing_signup/', views.marketing_signup, name='marketing_signup'),
    path('marketing_unsubscribe/', views.marketing_unsubscribe, name='marketing_unsubscribe'),
]