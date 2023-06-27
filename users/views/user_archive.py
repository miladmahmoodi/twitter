from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, logout

from users.models import User


def user_archive_view(request, username):
    """

    :param request:
    :param username:
    :return:
    """
    if request.user.username == username:
        user = User.objects.filter(
            username=username,
        )
        if user:
            user.delete()
            logout(request)

        return redirect(
            '/explore/',
        )
