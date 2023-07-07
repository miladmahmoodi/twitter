from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from  django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

from posts.models import Post, Comment
from posts.forms import CommentForm
from core.utils import UsersMessages

User = get_user_model()


class CommentReplyView(LoginRequiredMixin, View):
    """

    """
    form_class = CommentForm

    def setup(self, request, *args, **kwargs):
        self.this_user = get_object_or_404(
            User,
            is_active=True,
            pk=request.user.pk,
        )
        self.this_post = get_object_or_404(
            Post,
            is_active=True,
            pk=kwargs.get('pk'),
        )
        self.this_parent = get_object_or_404(
            Comment,
            pk=kwargs.get('comment_pk'),
        )
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        form = self.form_class(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user=self.this_user,
                post=self.this_post,
                parent=self.this_parent,
                text=form.cleaned_data.get('text'),
            )
            self.this_post.add_post_comment()
            level = messages.SUCCESS
            message = UsersMessages.comment_successfully
        else:
            level = messages.ERROR
            message = UsersMessages.comment_failed

        messages.add_message(
            request,
            level=level,
            message=message,
        )
        return redirect(
            'post:post_detail',
            pk=kwargs.get('pk'),
        )
