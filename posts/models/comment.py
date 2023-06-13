from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


class Comment(BaseModel):
    """

    """

    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('parent'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    text = models.CharField(
        verbose_name=_('text'),
        max_length=2_200,
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
        return self.text
