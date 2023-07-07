from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from core.utils import UsersMessages
from posts.models import Post


class PostArchiveView(LoginRequiredMixin, View):
    """

    """

    def setup(self, request, *args, **kwargs):
        self.this_post = get_object_or_404(
            Post,
            is_active=True,
            pk=kwargs.get('pk'),
        )
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.this_post.user:
            return HttpResponseForbidden(
                UsersMessages.update_profile_forbidden,
            )
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # self.this_post.post_count -= 1
        # self.this_post.save()
        self.this_post.delete()

        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=UsersMessages.post_archive_successfully,
        )
        return redirect(
            'user:user_detail',
            pk=request.user.pk,
        )

