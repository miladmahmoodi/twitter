from django.contrib import admin
from ..models import Post, Image


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

    list_display = [
        'id',
        'title',
        'slug',
        'caption',
        'likes_count',
        'comments_count',
        'is_active',
        'created_at',
    ]
    search_fields = [
        'title',
    ]
    list_filter = [
        'created_at',
    ]
    prepopulated_fields = {
        "slug": ("title",)
    }
    readonly_fields = (
        'likes_count',
        'comments_count',
    )
    inlines = [
        TagInline,
        ImageInline,
    ]
