from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('product_details/', views.details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>', views.cart_add, name='cart_add'),
    path('cart/remove/<int:cart_id>', views.cart_remove, name='cart_remove'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
