from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel, TimeStampMixin
from django.contrib.auth.models import AbstractBaseUser


class User(TimeStampMixin, AbstractBaseUser, BaseModel):
    username = models.CharField(
        verbose_name=_('username'),
        max_length=50,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=70,
    )
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=254,
    )
    password = models.CharField(
        verbose_name=_('password'),
        max_length=128,
    )
    bio = models.CharField(
        verbose_name=_('biography'),
        max_length=100,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='user/images/',
        null=True,
        blank=True,
    )
    followers_count = models.PositiveIntegerField(
        verbose_name=_('followers count'),
        default=0,
    )
    following_count = models.PositiveIntegerField(
        verbose_name=_('following count'),
        default=0,
    )
    post_count = models.PositiveIntegerField(
        verbose_name=_('post count'),
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name=_('is active'),
        default=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    'username',
                ],
                name='username_index',
            ),
        ]
