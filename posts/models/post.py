from django.db import models
from core.models import SoftDeleteModel, TimeStampMixin
from django.utils.translation import gettext as _


class Post(TimeStampMixin, SoftDeleteModel):
    """

    """

    class StatusChoice(models.TextChoices):
        """

        """
        ACTIVE = 'A', _('active')
        INACTIVE = 'I', _('inactive')

    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
        unique=True,
    )
    caption = models.CharField(
        verbose_name=_('caption'),
        max_length=2_200,
    )
    tag = models.ManyToManyField(
        'posts.Tag',
        related_name='tags',
        verbose_name=_('tag'),
        null=True,
        blank=True,
        editable=False,
    )
    likes_count = models.PositiveIntegerField(
        verbose_name=_('likes count'),
        default=0,
    )
    comments_count = models.PositiveIntegerField(
        verbose_name=_('comments count'),
        default=0,
    )

    def is_like_by_user(self, user):
        """

        :param user:
        :return:
        """
        return self.likes.filter(
            user=user
        ).exists()

    def add_post_like(self):
        """

        :return:
        """
        self.likes_count += 1
        self.save()

    def remove_post_like(self):
        """

        :return:
        """
        if self.likes_count > 0:
            self.likes_count -= 1
            self.save()

    def __str__(self):
        return self.title
