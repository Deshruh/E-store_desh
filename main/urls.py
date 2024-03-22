from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about_us/', views.about_us),
    path('contacts/', views.contacts),
    path('login/', views.login)
]