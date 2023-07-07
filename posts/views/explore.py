from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from posts.models import Post
from users.forms import SearchForm


class ExploreListView(LoginRequiredMixin, ListView):
    """

    """

    model = Post
    context_object_name = 'posts'
    template_name = 'posts/explore.html'
    paginate_by = 3

    # @method_decorator(user_passes_test(lambda u: True))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        context = Post.objects.exclude(
            user=self.request.user,
        )
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context
