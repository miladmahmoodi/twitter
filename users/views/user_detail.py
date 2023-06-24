from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


def user_detail_view(request, username):
    """

    :param request:
    :param username:
    :return:
    """
    user = get_object_or_404(
        User,
        username=username,
        is_active=True,
    )
    posts = user.posts.all()
    context = {
        'user': user,
        'posts': posts,
    }
    return render(
        request,
        template_name='users/user-detail.html',
        context=context,
    )
