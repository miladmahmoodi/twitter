from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from posts.models import Tag, Post, TagRelation
from users.models import User
from core.utils import UsersMessages


class TagPostsListView(LoginRequiredMixin, ListView):
    """

    """

    model = Post
    context_object_name = 'posts'
    template_name = 'posts/tag-posts-list.html'
    paginate_by = 3

    def setup(self, request, *args, **kwargs):
        self.this_tag = Tag.objects.filter(
            pk=kwargs.get('pk'),
        ).first()
        self.this_user = User.objects.filter(
            pk=request.user.pk,
        ).first()
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        context = Post.objects.filter(
            tag=self.this_tag,
        )
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.this_tag

        is_following = TagRelation.objects.filter(
            from_user=self.this_user,
            to=self.this_tag,
        ).exists()
        if is_following:
            context['is_following'] = is_following

        return context

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        tag_relation = TagRelation.objects.filter(
            from_user=self.this_user,
            to=self.this_tag,
        )
        if not tag_relation.exists():
            TagRelation.objects.create(
                from_user=self.this_user,
                to=self.this_tag,
            )
            level = messages.SUCCESS
            message = UsersMessages.tag_follow_successfully
        else:
            tag_relation.delete()
            level = messages.SUCCESS
            message = UsersMessages.tag_unfollow_successfully

        messages.add_message(
            request,
            level=level,
            message=message,
        )
        return redirect(
            'post:tag_posts',
            pk=kwargs.get('pk'),
        )
