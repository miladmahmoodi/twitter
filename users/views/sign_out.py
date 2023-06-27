from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, logout


def signout_view(request):
    """

    :param request:
    :return:
    """
    logout(request)
    return redirect(
        '/explore/',
    )
