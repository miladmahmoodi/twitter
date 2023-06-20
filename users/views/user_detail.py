from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


def user_detail_view(request, username):
    """

    :param request:
    :param username:
    :return:
    """
    user = User.objects.get(
        username=username,
        is_active=True,
    )
    context = {
        'user': user,
    }
    return render(
        request,
        template_name='users/user-detail.html',
        context=context,
    )
