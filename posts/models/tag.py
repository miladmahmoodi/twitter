from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _


class Tag(BaseModel):
    """

    """

    creator = models.ForeignKey(
        'users.User',
        verbose_name=_('creator'),
        on_delete=models.PROTECT,
        related_name='tags',
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True,
    )

    def tag_posts(self):
        """

        :return:
        """
        return self.posts.all()

    def tag_post_count(self):
        """

        :return:
        """
        return self.posts.count()

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    'name',
                ],
                name='name_index',
            ),
        ]
