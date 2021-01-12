from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name" ,"username", "password1"]
        help_texts = {
            'username': None,
            'password1': None,
        }