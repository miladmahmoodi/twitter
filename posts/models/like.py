from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Like(BaseModel):
    """

    """

    user = models.ForeignKey(
        'User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        'posts.Post',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='likes'
    )

    def __str__(self):
        return f'{self.user} liked {self.post}'
