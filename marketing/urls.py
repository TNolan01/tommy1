from django.urls import path
from . import views

urlpatterns = [
    path(
        'marketing_signup/',
        views.marketing_signup,
        name='marketing_signup'),
    path(
        'marketing_unsubscribe/',
        views.marketing_unsubscribe,
        name='marketing_unsubscribe'),
    path(
        'newsletter/',
        views.newsletter,
        name='newsletter'),
    path(
        'email_list/',
        views.email_list,
        name='email_list'),
    path(
        'remove_subscriber/<int:customer_id>/',
        views.remove_subscriber,
        name='remove_subscriber'),
    path(
        'send_newsletter/',
        views.send_newsletter,
        name='send_newsletter'),
]
