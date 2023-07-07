from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel
from django.contrib.auth import get_user_model


User = get_user_model


class TagRelation(BaseModel):
    from_user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name=_('from user'),
        related_name='following_tags'
    )
    to = models.ForeignKey(
        'posts.Tag',
        on_delete=models.CASCADE,
        verbose_name=_('to tag'),
    )

    def __str__(self):
        return f'{self.from_user} following {self.to}'
