from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as  _


class Post(BaseModel):
    """

    """

    user = models.ForeignKey(
        'user.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
    )
    image = models.ForeignKey(
        'Image',
        on_delete=models.CASCADE,
        verbose_name=_('image'),
    )
    caption = models.CharField(
        verbose_name=_('caption'),
        max_length=2_200,
    )
    tag = models.ManyToManyField(
        'tag',
        verbose_name=_('tag'),
    )
    comment = models.ForeignKey(
        'comment',
        on_delete=models.PROTECT,
        verbose_name=_('comment'),
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
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )


class Tag(BaseModel):
    creator = models.ForeignKey(
        'users.User',
        verbose_name=_('creator'),
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )


class Comment(BaseModel):
    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('parent'),
        on_delete=models.CASCADE,
    )
    text = models.CharField(
        verbose_name=_('text'),
        max_length=2_200,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )


class Like(BaseModel):
    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post',
        verbose_name=_('user'),
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )


class Image(BaseModel):
    post = models.ForeignKey(
        'Posts',
        verbose_name=_('post'),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='post/images/',
    ),
    alt = models.CharField(
        verbose_name=_('alternative'),
        max_length=100,
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )




