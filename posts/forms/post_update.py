from django import forms
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

from posts.models import Post, Image


class PostUpdateForm(forms.ModelForm):
    image_name = forms.CharField(
        label=_('image name'),
        required=False,
    )
    image_alt = forms.CharField(
        label=_('image alternative'),
        required=False,
    )
    image = forms.ImageField(
        label=_('Image'),
        required=False,
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'caption',
            'tag',
        ]

    def clean(self):
        """

        :return:
        """
        cleaned_data = super().clean()

        post = get_object_or_404(
            Post,
            title=cleaned_data.get('title'),
            caption=cleaned_data.get('caption'),
        )

        image = Image.objects.filter(
            name=cleaned_data.get('image_name'),
            alt=cleaned_data.get('image_alt'),
            image=cleaned_data.get('image'),
        )
        if not image.exists():
            Image.objects.create(
                post=post,
                name=cleaned_data.get('image_name'),
                alt=cleaned_data.get('image_alt'),
                image=cleaned_data.get('image'),
            )
        return cleaned_data
