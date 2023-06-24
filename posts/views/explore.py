from django.shortcuts import render
from ..models import Post


def explore_view(request):
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
        template_name='posts/explore.html',
        context=context,
    )
