from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


class Like(BaseModel):
    """

    """

    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
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
        return f'{self.user} liked {self.post}'
