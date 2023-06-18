from django.contrib import admin
from ..models import Post, Tag, Image


class TagInline(admin.TabularInline):
    """

    """

    model = Post.tag.through
    extra = 1


class ImageInline(admin.TabularInline):
    """

    """

    model = Image
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """

    """
    inlines = [
        TagInline,
        ImageInline,
    ]
