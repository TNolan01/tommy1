from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.all_products,
        name='products'),
    path(
        'special_offers',
        views.special_offers,
        name='special_offers'),
    path(
        '<int:product_id>/',
        views.product_detail,
        name='product_detail'),
    path(
        'add/',
        views.add_product,
        name='add_product'),
    path(
        'edit/<int:product_id>/',
        views.edit_product,
        name='edit_product'),
    path(
        'delete_product/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
]
