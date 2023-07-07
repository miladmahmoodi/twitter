from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from itertools import chain

from users.models import User
from users.forms import SearchForm
from posts.models import Post


class HomeView(LoginRequiredMixin, ListView):
    """

    """

    model = User
    paginate_by = 3
    template_name = 'users/home.html'
    context_object_name = 'posts'

    def setup(self, request, *args, **kwargs):
        self.this_user = get_object_or_404(
            User,
            pk=request.user.pk,
        )
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        following_user = self.this_user.following.all()
        following_tag = self.this_user.following_tags.all()

        following_users = [
            user.to for user in following_user
        ]
        following_tags = [
            tag.to for tag in following_tag
        ]

        posts = Post.objects.filter(
            user__in=following_users,
        )
        tag_posts = Post.objects.filter(
            tag__in=following_tags,
        )
        posts_data = posts | tag_posts

        return posts_data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context
