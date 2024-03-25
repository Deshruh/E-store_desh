from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
                attrs = {
                    "name": "name",
                    "placeholder": "User Name"
                }
            )
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
                attrs = {
                    "name": "password",
                    "placeholder": "Your Password"
                }
            )
        )
    class Meta:
        models = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
                attrs = {
                    "name": "full-name",
                    "placeholder": "Your Name"
                }
            )
        )
    username = forms.CharField(
        widget=forms.TextInput(
                attrs = {
                    "name": "name",
                    "placeholder": "User Name"
                }
            )
        )
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
                attrs = {
                    "name": "phone",
                    "placeholder": "Phone"
                }
            )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
                attrs = {
                    "name": "email",
                    "placeholder": "Email"
                }
            )
        )  
    password1 = forms.CharField(
        widget=forms.PasswordInput(
                attrs = {
                    "name": "password",
                    "placeholder": "Password"
                }
            )
        )    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
                attrs = {
                    "name": "retype-password",
                    "placeholder": "Re Password"
                }
            )
        )   
    class Meta:
        model = User
        fields = ('first_name', 'username', "phone_number", "email", "password1", "password2")