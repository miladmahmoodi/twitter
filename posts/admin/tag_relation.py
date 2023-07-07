from django.contrib import admin

from posts.models import TagRelation


@admin.register(TagRelation)
class TagRelationAdmin(admin.ModelAdmin):
    """

    """

    pass
