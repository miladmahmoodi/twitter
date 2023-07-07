from django import forms
from django.contrib.auth import authenticate, login

from core.utils import UsersMessages


class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Username',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
