from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect as redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


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
                return redirect(reverse("profile"))
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
            messages.success(request, 'Congratulations! You registrated success!')
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

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile changed success')
            return redirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        "banner": True,
        "banner_image": False,
        "name_page": "Profile",

        "form": form
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))
