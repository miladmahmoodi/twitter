from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model

from posts.models import Post


User = get_user_model()


def home_view(request):
    """

    :param request:
    :return:
    """
    posts = Post.objects.all()
    return HttpResponse(posts)
