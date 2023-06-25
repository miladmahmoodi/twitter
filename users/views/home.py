from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


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
    following = user.following.all()
    context = {
        'following': following,
    }

    return render(
        request,
        template_name='users/home.html',
        context=context,
    )
