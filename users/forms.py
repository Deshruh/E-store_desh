from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
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


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), required=False)
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-label'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'status', 'phone_number', 'image')
