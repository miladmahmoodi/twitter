from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import get_user_model

from posts.models import Post


User = get_user_model()


def post_detail_view(request, username, post_id):
    """

    :param request:
    :param username:
    :param post_id:
    :return:
    """
    post = get_object_or_404(
        Post,
        id=post_id,
        user__username=username,
    )
    tags = post.tag.all()
    context = {
        'post': post,
        'tags': tags,
    }
    return render(
        request,
        template_name='users/user-post-detail.html',
        context=context,
    )
