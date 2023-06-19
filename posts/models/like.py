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
        related_name='likes'
    )
    post = models.ForeignKey(
        'posts.Post',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
        related_name='likes'
    )

    def __str__(self):
        return f'{self.user} liked {self.post.title} from {self.post.user}'
