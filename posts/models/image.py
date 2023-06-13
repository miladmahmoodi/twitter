from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


class Image(BaseModel):
    """

    """

    post = models.ForeignKey(
        'Posts',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='post/images/',
    ),
    alt = models.CharField(
        verbose_name=_('alternative'),
        max_length=100,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )

    def __str__(self):
        return f'{self.post} - {self.alt}'