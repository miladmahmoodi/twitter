from django.forms import inlineformset_factory, ModelForm
from posts.models import Post, Image


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'caption',
            'tag',
        ]


class ImageCreateForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


ImageCreateFormSet = inlineformset_factory(
    Post,
    Image,
    fields='__all__',
    extra=1,
)
