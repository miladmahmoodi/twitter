from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class ChangePasswordView(PasswordChangeView):
    template_name = 'users/change-password.html'
    success_url = reverse_lazy('user:user_detail')
