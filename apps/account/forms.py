from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email","first_name","last_name",'password1','password2']


class LoginForm(AuthenticationForm):
	username = forms.CharField(label='Email')
