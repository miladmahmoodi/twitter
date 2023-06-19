from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


class Image(BaseModel):
    """

    """

    post = models.ForeignKey(
        'posts.Post',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
        related_name='images',
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=75,
    )
    alt = models.CharField(
        verbose_name=_('alternative'),
        max_length=100,
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='post/images/',
    )

    def __str__(self):
        return self.name
