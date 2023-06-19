from django.contrib import admin
from ..models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """

    """
    list_display = [
        'id',
        'user',
        'post',
        'parent',
        'text',
        'created_at',
    ]
    search_fields = [
        'user__username',
    ]
    list_filter = [
        'created_at',
    ]