from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext as _
from core.models import SoftDeleteModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, SoftDeleteModel):
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
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

    def add_followers_count(self):
        """

        :return:
        """
        self.followers_count += 1
        self.save()

    def min_followers_count(self):
        """

        :return:
        """
        if self.followers_count > 0:
            self.followers_count -= 1
            self.save()

    def add_following_count(self):
        """

        :return:
        """
        self.following_count += 1
        self.save()

    def min_following_count(self):
        """

        :return:
        """
        if self.following_count > 0:
            self.following_count -= 1
            self.save()

    def add_post_count(self):
        """

        :return:
        """
        self.post_count += 1
        self.save()

    def min_post_count(self):
        """

        :return:
        """
        if self.post_count > 0:
            self.post_count -= 1
            self.save()

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


class UserRecycle(User):

    objects = Manager()

    class Meta:
        proxy = True
