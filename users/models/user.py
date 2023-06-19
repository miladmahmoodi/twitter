from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel, TimeStampMixin
from core.utils.base_errors import BaseError
from django.contrib.auth.models import AbstractUser, BaseUserManager


# class UserManager(BaseUserManager):
#     """
#
#     """
#
#     def create_user(self, username: str = None, password: str = None):
#         """
#
#         :param username:
#         :param password:
#         :return:
#         """
#         if not username:
#             raise ValueError(BaseError.user_must_have_username)
#         user = self.model(
#             username=username,
#         )
#         user.set_password(password)
#         user.save(
#             using=self._db,
#         )
#         return user
#
#     def create_staffuser(self, username: str = None, password: str = None):
#         """
#
#         :param username:
#         :param password:
#         :return:
#         """
#         if not username:
#             raise ValueError(BaseError.user_must_have_username)
#         user = self.model(
#             username=username,
#         )
#         user.set_password(password)
#         user.staff = True
#         user.save(
#             using=self._db,
#         )
#         return user
#
#     def create_superuser(self, username: str = None, password: str = None):
#         """
#
#         :param username:
#         :param password:
#         :return:
#         """
#
#         if not username:
#             raise ValueError(BaseError.user_must_have_username)
#         user = self.model(
#             username=username,
#         )
#         user.set_password(password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.is_active = True
#         user.save(
#             using=self._db,
#         )
#         return user


class User(TimeStampMixin, AbstractUser, BaseModel):
    # username = models.CharField(
    #     verbose_name=_('username'),
    #     max_length=50,
    #     unique=True,
    # )
    # first_name = models.CharField(
    #     verbose_name=_('first name'),
    #     max_length=50,
    # )
    # last_name = models.CharField(
    #     verbose_name=_('last name'),
    #     max_length=70,
    # )
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
    )
    # password = models.CharField(
    #     verbose_name=_('password'),
    #     max_length=128,
    # )
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
