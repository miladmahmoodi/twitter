from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext as _
from uuid import uuid4


class SoftQuerySet(QuerySet):
    def delete(self):
        return self.update(
            is_active=False,
        )


class SoftManager(models.Manager):
    """

    """
    def get_queryset(self):
        return SoftQuerySet(
            self.model,
            self._db,
        ).filter(
            is_active=True,
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

    def delete(self, using=None, keep_parents=False):
        """

        :param using:
        :param keep_parents:
        :return:
        """

        self.is_active = False
        self.save()

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    """

    """

    is_active = models.BooleanField(
        verbose_name=_('is active'),
        default=True,
    )

    objects = SoftManager()
    
    def delete(self, using=None, keep_parents=False):
        """
        
        :param using: 
        :param keep_parents: 
        :return: 
        """
        
        self.is_active = False
        self.save()

    class Meta:
        abstract = True
    #     indexes = [
    #         models.Index(
    #             fields=[
    #                 'is_active',
    #             ],
    #             name='is_active_index',
    #         ),
    #     ]


class TimeStampMixin:
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )
