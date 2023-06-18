from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _


class Image(BaseModel):
    """

    """

    post = models.ForeignKey(
        'posts.Posts',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='post/images/',
    ),
    alt = models.CharField(
        verbose_name=_('alternative'),
        max_length=100,
    )

    def __str__(self):
        return f'{self.post} - {self.alt}'
