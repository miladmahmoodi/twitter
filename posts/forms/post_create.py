from django import forms
from posts.models import Post, Image


class PostCreateForm(forms.ModelForm):
    tags = forms.CharField(
        label='Tags',
        required=False,
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'caption',
        ]


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


ImageCreateFormSet = forms.inlineformset_factory(
    parent_model=Post,
    model=Image,
    fields='__all__',
    extra=3,
    max_num=5,
)
