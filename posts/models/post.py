from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _

from . import Like, Comment, Tag


class Post(TimeStampMixin, BaseModel):
    """

    """

    user = models.ForeignKey(
        'user.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
    )
    caption = models.CharField(
        verbose_name=_('caption'),
        max_length=2_200,
    )
    likes_count = models.PositiveIntegerField(
        verbose_name=_('likes count'),
        default=0,
    )
    comments_count = models.PositiveIntegerField(
        verbose_name=_('comments count'),
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name=_('is active'),
        default=True,
    )

    def get_user_likes(self):
        """

        :return:
        """
        return Like.objects.filter(
            post=self.id,
        )

    def get_post_comments(self):
        """

        :return:
        """
        return Comment.objects.filter(
            post=self.id,
        )

    def get_post_tags(self):
        """

        :return:
        """
        return self.tags.all()

    def __str__(self):
        return f'{self.user} - {self.title}'
