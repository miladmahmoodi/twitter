from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """

    """
    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        ]
    list_filter = ['username']
    filter_horizontal = ()
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                "first_name",
                "last_name",
                "email",
                'image',
                'bio',
                'followers_count',
                'following_count',
                'post_count',
            )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = [
        'followers_count',
        'following_count',
        'post_count',
    ]
