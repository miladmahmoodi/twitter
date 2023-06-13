from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


class Tag(BaseModel):
    """

    """

    creator = models.ForeignKey(
        'users.User',
        verbose_name=_('creator'),
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True,
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
        return self.name
