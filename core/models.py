from django.db import models
from django.utils.translation import gettext as _
from uuid import uuid4


class MyManager(models.Manager):
    """

    """

    def get_queryset(self):
        """

        :return:
        """
        return super().get_queryset().filter(
            is_active=True,
        )

    def archives(self):
        """

        :return:
        """

        return super().get_queryset().filter(
            is_active=False,
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
    
    def delete(self, using=None, keep_parents=False):
        """
        
        :param using: 
        :param keep_parents: 
        :return: 
        """
        
        self.is_active = False,
        self.save()

    class Meta:
        abstract = True


class TimeStampMixin:
    update_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )
