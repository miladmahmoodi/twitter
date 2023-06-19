from django.contrib import admin
from ..models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """

    """
    list_display = [
        'id',
        'name',
        'alt',
        'image',
        'post',
        'created_at',
    ]
    search_fields = [
        'name',
        'alt',
    ]
    list_filter = [
        'created_at',
    ]
