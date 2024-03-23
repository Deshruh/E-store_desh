from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name = 'catalog'),
    path('product_details/', views.details, name ='product_details'),
    path('cart/', views.cart, name = 'cart'),
    path('wishlist/', views.wishlist, name = 'wishlist'),
]