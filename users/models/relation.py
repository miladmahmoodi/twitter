from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel, TimeStampMixin


class Relation(TimeStampMixin, BaseModel):
    from_user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name=_('from user'),
        related_name='following',
    )
    to_user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name=_('to user'),
        related_name='followers',
    )

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'
