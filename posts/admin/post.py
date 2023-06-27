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
        'user',
        'title',
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
    readonly_fields = (
        'likes_count',
        'comments_count',
        'is_active',
    )
    inlines = [
        TagInline,
        ImageInline,
    ]
    actions = [
        'deactivate_post',
        'activate_post',
    ]

    def delete_queryset(self, request, queryset):
        """

        :param request:
        :param queryset:
        :return:
        """

        queryset.update(
            is_active=False,
        )
        self.message_user(
            request,
            'posts successfully deactivate.',
        )

    @admin.action(
        description='Activate selected posts',
    )
    def activate_post(self, request, queryset):
        """

        :param request:
        :param queryset:
        :return:
        """

        queryset.update(
            is_active=True,
        )
        self.message_user(
            request,
            'posts successfully activate.',
        )