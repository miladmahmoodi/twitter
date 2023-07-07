from django import forms

from users.models import User
from core.utils import UsersMessages


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'image',
        ]