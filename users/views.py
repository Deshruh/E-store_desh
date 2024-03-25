from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect as redirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        data = request.POST
        form = UserLoginForm(data=data)
        if form.is_valid():
            username = data['username']
            password = data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse("home"))
    else:
        form = UserLoginForm()

    context = {
        "banner": True,
        "banner_image": False,
        "name_page": "Login",

        "form": form
    }
    return render(request, "users/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()

    context = {
        "banner": True,
        "banner_image": False,
        "name_page": "Registration",

        "form": form
    }
    return render(request, "users/registration.html", context)