from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from posts.models import Post, Comment
from users.models import User


def register_view(request):
    """

    :param request:
    :return:
    """

    if request.method == 'GET':
        return render(
            request,
            template_name='users/register.html',
        )

    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(
            username=data.get('username'),
        ).exists()

        if not user:
            if data.get('password') == data.get('confirm_password'):
                new_user = User.objects.create_user(
                    username=data.get('username'),
                    email=data.get('email'),
                    password=data.get('password'),
                )


            return redirect(
                '/signin/',
            )


