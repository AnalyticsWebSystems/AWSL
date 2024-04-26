from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "John Doe",
        "class": "form-control"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "example@gmail.com",
        "class": "form-control"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "quick brown fox",
        "class": "form-control"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "quick brown fox",
        "class": "form-control"
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "example@gmail.com"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "quick brown fox jump"
    }))
