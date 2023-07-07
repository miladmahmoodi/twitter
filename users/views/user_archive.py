from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth import logout

from users.models import User
from core.utils import UsersMessages


class UserArchiveView(LoginRequiredMixin, View):
    """

    """

    def setup(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.this_suer = get_object_or_404(
            User,
            pk=kwargs.get('pk'),
        )
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user != self.this_suer:
            return HttpResponseForbidden(
                    UsersMessages.archive_profile_forbidden,
                )
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        self.this_suer.delete()
        logout(request)
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=UsersMessages.archive_profile_successfully,
        )
        return redirect(
            'post:explore',
        )

# def user_archive_view(request, username):
#     """
#
#     :param request:
#     :param username:
#     :return:
#     """
#     if request.user.username == username:
#         user = User.objects.filter(
#             username=username,
#         )
#         if user:
#             user.delete()
#             logout(request)
#
#         return redirect(
#             '/explore/',
#         )
