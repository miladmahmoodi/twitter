from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from users.models import User


def edit_profile_view(request, username):
    """

    :param request:
    :param username:
    :return:
    """

    user = get_object_or_404(
        User,
        username=username,
    )

    if request.method == 'GET':
        context = {
            'user': user,
        }
        return render(
            request,
            template_name='users/edit-profile.html',
            context=context,
        )

    if request.method == 'POST':

        data = request.POST
        user.username = data.get('username')
        user.email = data.get('email')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.bio = data.get('bio')
        user.save()

        return redirect(
            f'/{user.username}/',
        )
