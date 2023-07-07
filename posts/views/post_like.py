from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from posts.models import Post, Like
from core.utils import UsersMessages

User = get_user_model()


class PostLikeView(LoginRequiredMixin, View):
    """

    """

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:
        """

        post = get_object_or_404(
            Post,
            is_active=True,
            pk=pk,
        )
        user = get_object_or_404(
            User,
            is_active=True,
            pk=request.user.pk,
        )

        if not post.is_like_by_user(user):
            Like.objects.create(
                user=user,
                post=post,
            )
            post.add_post_like()
            level = messages.SUCCESS
            message = UsersMessages.like_successfully
        else:
            level = messages.ERROR
            message = UsersMessages.like_Error

        messages.add_message(
            request,
            level=level,
            message=message,
        )
        return redirect(
            'post:post_detail',
            pk=pk,
        )