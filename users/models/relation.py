from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel
from django.contrib.auth import get_user_model


User = get_user_model


class Relation(BaseModel):
    from_user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        verbose_name=_('from user'),
        related_name='following',
    )
    to = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        verbose_name=_('to user'),
        related_name='followers',
    )

    @staticmethod
    def is_following(user, other):
        """

        :param user:
        :param other:
        :return:
        """
        return Relation.objects.filter(
            from_user=user,
            to=other,
        ).exists()

    def __str__(self):
        return f'{self.from_user} following {self.to}'
