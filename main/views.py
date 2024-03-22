from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def login(request):
    return render(request, "main/login-register.html")


def about_us(request):
    return render(request, "main/about.html")


def contacts(request):
    return render(request, "main/contact.html")