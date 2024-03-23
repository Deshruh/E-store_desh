from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name = 'articles'),
    path('article_details', views.article_details, name = 'article_details'),
]