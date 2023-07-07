from django import forms


class SearchForm(forms.Form):
    """

    """

    search = forms.CharField(
        max_length=125,
        label='Search',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search username...',
            },
        )
    )
