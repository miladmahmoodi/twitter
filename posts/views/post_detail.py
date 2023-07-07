from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

from posts.models import Post, Comment
from posts.forms import CommentForm
from core.utils import UsersMessages

User = get_user_model()


class PostDetailView(LoginRequiredMixin, View):
    """

    """

    template_name = 'posts/post-detail.html'
    form_class = CommentForm

    def setup(self, request, *args, **kwargs):
        self.this_post = get_object_or_404(
            Post,
            is_active=True,
            pk=kwargs.get('pk'),
        )
        return super().setup(request, *args, **kwargs)

    def get(self, request, pk):
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
        tags = post.tag.all()
        context = {
            'post': post,
            'is_like': post.is_like_by_user(request.user),
            'form': self.form_class(),
            'tags': tags,
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        comment_form = self.form_class(request.POST)

        if comment_form.is_valid():
            Comment.objects.create(
                user=request.user,
                post=self.this_post,
                text=comment_form.cleaned_data.get('text'),
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
