from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect

from posts.models import Tag, Post
from users.models import Relation


class TagPostsDetailView(LoginRequiredMixin, View):
    """

    """

    template_name = 'posts/tag-posts.html'

    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:
        """

        tag = get_object_or_404(
            Tag,
            pk=pk,
        )
        posts = Post.objects.filter(
            tag=tag,
        )
        context = {
            'tag': tag,
            'posts': posts,
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:
        """

        relation = get_object_or_404(
            Relation,

        )


class TagPostsListView(LoginRequiredMixin, ListView):
    """

    """

    model = Post
    context_object_name = 'posts'
    template_name = 'posts/tag-posts.html'
    paginate_by = 3

    def setup(self, request, *args, **kwargs):
        self.this_tag = get_object_or_404(
            Tag,
            pk=kwargs.get('pk'),
        )
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        context = Post.objects.filter(
            tag=self.this_tag,
        )
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.this_tag
        return context
