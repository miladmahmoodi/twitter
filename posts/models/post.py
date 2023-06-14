from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _


class Post(TimeStampMixin, BaseModel):
    """

    """

    user = models.ForeignKey(
        'user.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
    )
    image = models.ForeignKey(
        'Image',
        on_delete=models.CASCADE,
        verbose_name=_('image'),
        null=True,
        blank=True,
    )
    caption = models.CharField(
        verbose_name=_('caption'),
        max_length=2_200,
    )
    tag = models.ManyToManyField(
        'tag',
        verbose_name=_('tag'),
        null=True,
        blank=True,
    )
    comment = models.ForeignKey(
        'comment',
        on_delete=models.PROTECT,
        verbose_name=_('comment'),
        null=True,
        blank=True,
    )
    likes_count = models.PositiveIntegerField(
        verbose_name=_('likes count'),
        default=0,
    )
    comments_count = models.PositiveIntegerField(
        verbose_name=_('comments count'),
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name=_('is active'),
        default=True,
    )

    def __str__(self):
        return f'{self.user} - {self.title}'
