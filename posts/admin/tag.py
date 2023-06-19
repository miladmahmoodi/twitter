from django.contrib import admin
from ..models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """

    """
    list_display = [
        'id',
        'name',
        'created_at',
    ]
    search_fields = [
        'name',
    ]
    list_filter = [
        'created_at',
    ]
