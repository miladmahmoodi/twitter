from django.contrib import admin
from users.models import Relation


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    """

    """

    pass
