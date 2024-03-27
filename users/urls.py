from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
<<<<<<< HEAD
    path('registration/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.logout, name = 'logout')
=======
    path('registration/', views.register, name = 'register')
>>>>>>> e0ea8df6e5c80f6970e106a9500bf4df3f1aefdb
]