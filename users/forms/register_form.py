from django import forms
from django.core.exceptions import ValidationError

from users.models import User
from core.utils import UsersMessages


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Username',
    )
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        required=True,
        label='Confirm password',
        widget=forms.PasswordInput(),
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(
            username=username,
        ).exists()
        if user:
            raise ValidationError(
                UsersMessages.username_exists,
            )
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                UsersMessages.confirm_password_err
            )
