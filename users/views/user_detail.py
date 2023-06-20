from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()


def user_detail(request, username):
    """

    :param request:
    :param username:
    :return:
    """
    user = User.objects.get(username=username)
    return HttpResponse(user.get_full_name())