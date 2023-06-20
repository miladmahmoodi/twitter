from django.shortcuts import render
from django.contrib.auth import get_user_model

from posts.models import Post


User = get_user_model()


def home_view(request):
    """

    :param request:
    :return:
    """
    posts = Post.objects.filter(
        is_active=True,
    )
    context = {
        'posts': posts,
    }
    return render(
        request,
        template_name='users/home.html',
        context=context,
    )
