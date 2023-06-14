from django.db import models
from django.utils.translation import gettext as _
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimeStampMixin:
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )
