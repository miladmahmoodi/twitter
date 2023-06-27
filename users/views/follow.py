from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from users.models import User, Relation


def follow_view(request, username):
    """

    :param request:
    :param username:
    :return:
    """

    user = get_object_or_404(
        User,
        username=username,
    )
    is_follow = Relation.objects.filter(
        from_user=request.user,
        to_user=user,
    ).exists()
    if not is_follow:
        Relation.objects.create(
            from_user=request.user,
            to_user=user,
        )

    return redirect(
        f'/{user}/',
    )
