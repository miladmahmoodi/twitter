from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(TimeStampMixin, BaseModel):
    """

    """

    user = models.ForeignKey(
        'User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    post = models.ForeignKey(
        'posts.Post',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('parent'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )
    text = models.CharField(
        verbose_name=_('text'),
        max_length=2_200,
    )

    def __str__(self):
        return self.text

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    'text',
                ],
                name='text_index',
            ),
        ]