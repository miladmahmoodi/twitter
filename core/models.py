from django.db import models
from django.utils.translation import gettext as _
from uuid import uuid4

from core.utils import StatusChoice


class MyManager(models.Manager):
    """

    """

    def get_queryset(self):
        """

        :return:
        """
        return super().get_queryset().filter(
            status='A',
        )

    def archives(self):
        """

        :return:
        """

        return super().get_queryset().filter(
            status='I',
        )


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    """

    """

    objects = MyManager()
    status = models.CharField(
        verbose_name=_('status'),
        max_length=1,
        choices=StatusChoice.choices,
        default=StatusChoice.ACTIVE,
        db_index=True,
    )
    
    def delete(self, using=None, keep_parents=False):
        """
        
        :param using: 
        :param keep_parents: 
        :return: 
        """
        
        self.status = 'I',
        self.save()

    class Meta:
        abstract = True


class TimeStampMixin:
    update_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )
