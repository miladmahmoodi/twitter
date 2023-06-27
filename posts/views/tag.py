from django.shortcuts import render
from django.shortcuts import get_object_or_404

from ..models import Tag
from ..models import Post


def tag_posts_view(request, tag_name):
    """

    :param request:
    :param tag_name:
    :return:
    """

    tag = get_object_or_404(
        Tag,
        name=tag_name,
    )
    tag_posts = Post.objects.filter(
        tag=tag,
    )
    context = {
        'tag': tag,
        'posts': tag_posts,
    }
    return render(
        request,
        template_name='posts/tag-posts.html',
        context=context,
    )
