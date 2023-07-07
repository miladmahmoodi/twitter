from django.views.generic import View
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import logout
from django.contrib import messages

from core.utils import UsersMessages


class SignOutView(View):
    """

    """

    def get(self, request):
        logout(
            request
        )
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=UsersMessages.signout_successfully,
        )
        return HttpResponseRedirect(
            settings.LOGIN_URL,
        )
