from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from posts.models import Post
from users.models import Relation


User = get_user_model()


def home_view(request):
    """

    :param request:
    :return:
    """

    user = get_object_or_404(
        User,
        username=request.user.username
    )
    users = user.following.all
    context = {
        'users': users,
    }

    return render(
        request,
        template_name='users/home.html',
        context=context,
    )
