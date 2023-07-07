from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Comment
from posts.forms import CommentForm


class CommentCreateView(LoginRequiredMixin, CreateView):
    """

    """

    model = Comment
    form_class = CommentForm