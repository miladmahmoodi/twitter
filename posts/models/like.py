from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _


class Like(TimeStampMixin, BaseModel):
    """

    """

    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        'Post',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='likes'
    )

    def __str__(self):
        return f'{self.user} liked {self.post}'
