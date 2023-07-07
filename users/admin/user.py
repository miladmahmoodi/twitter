from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from users.models import User, UserRecycle
from core.utils import AdminMessages


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
        'is_superuser',
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
        "last_login",
        "date_joined"
    ]

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


@admin.register(UserRecycle)
class UserAdmin(admin.ModelAdmin):
    """

    """

    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_superuser',
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
        (_("Important dates"), {
            "fields": (
                "last_login",
                "date_joined"
            ),
        },
         ),
    )
    readonly_fields = [
        'followers_count',
        'following_count',
        'post_count',
        "last_login",
        "date_joined"
    ]
    actions = [
        'activate_user',
    ]

    def get_queryset(self, request):
        return UserRecycle.objects.filter(
            is_active=False,
        )

    @admin.action(
        description=AdminMessages.user_activate_desc,
    )
    def activate_user(self, request, queryset):
        """

        :param request:
        :param queryset:
        :return:
        """

        queryset.update(
            is_active=True,
        )
