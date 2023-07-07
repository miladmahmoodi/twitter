from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User
from users.forms import EditProfileForm
from core.utils import UsersMessages


class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """

    """

    model = User
    template_name = 'users/edit-profile.html'
    form_class = EditProfileForm
    success_message = UsersMessages.update_profile_successfully

    def dispatch(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.pk != self.kwargs.get('pk'):
            return HttpResponseForbidden(
                UsersMessages.update_profile_forbidden,
            )
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(
            'user:user_detail',
            kwargs={
                'pk': self.object.pk,
            },
        )


