from django import forms

from posts.models import Comment


class CommentForm(forms.Form):
    """

    """

    text = forms.CharField(
        label='Comment',
        widget=forms.Textarea(
            attrs={
                'placeholder': "Your comment...",
            },
        ),
    )
