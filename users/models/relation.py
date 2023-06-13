from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel


class Relation(BaseModel):
    from_user = models.ManyToManyField(
        'User',
        verbose_name=_('from user'),
    )
    to_user = models.ManyToManyField(
        'User',
        verbose_name=_('to user'),
    )

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'
