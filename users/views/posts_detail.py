from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import get_user_model

from posts.models import Post, Comment
from users.models import User


def post_detail_view(request, username, post_id):
    """

    :param request:
    :param username:
    :param post_id:
    :return:
    """

    user = get_object_or_404(
        User,
        username=username,
    )
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
    if request.POST.get('comment'):
        Comment.objects.create(
            user=request.user,
            post=post,
            text=request.POST.get('comment'),
        )
    return render(
        request,
        template_name='users/user-post-detail.html',
        context=context,
    )
