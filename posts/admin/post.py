from django.contrib import admin
from django.utils.translation import gettext as _

from posts.models import Post, PostRecycle,  Image
from core.utils import AdminMessages


class ImageInline(admin.TabularInline):
    """

    """

    model = Image
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """

    """

    readonly_fields = (
        'likes_count',
        'comments_count',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_display = [
        'id',
        'user',
        'title',
        'caption',
        'likes_count',
        'comments_count',
        'is_active',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'title',
    ]
    list_filter = [
        'created_at',
    ]
    inlines = [
        ImageInline,
    ]
    fieldsets = (
        (None, {"fields": (
            "user",
            'title',
            'caption',
            'tag',
            'likes_count',
            'comments_count',
            'is_active',
            'created_at',
            'updated_at',
        )}),
    )

    def updated_at_formatted(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    updated_at_formatted.short_description = 'Updated at'

    # def delete_queryset(self, request, queryset):
    #     """
    #
    #     :param request:
    #     :param queryset:
    #     :return:
    #     """
    #
    #     queryset.update(
    #         is_active=False,
    #     )


@admin.register(PostRecycle)
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
        ImageInline,
    ]
    actions = [
        'deactivate_post',
        'activate_post',
    ]

    def get_queryset(self, request):
        return PostRecycle.objects.filter(
            is_active=False,
        )

    @admin.action(
        description=AdminMessages.post_activate_desc,
    )
    def activate_post(self, request, queryset):
        """

        :param queryset:
        :param request:
        :return:
        """

        queryset.update(
            is_active=True,
        )
