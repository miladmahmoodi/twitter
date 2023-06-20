from django.shortcuts import render, HttpResponse
from ..models import Post


def explore_view(request):
    """

    :param request:
    :return:
    """
    posts = Post.objects.filter(
        is_active=True,
    )
    return HttpResponse(posts)
