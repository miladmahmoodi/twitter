from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from core.utils import UsersMessages
from users.models import User, Relation


class UnfollowView(LoginRequiredMixin, View):
    """

    """

    def setup(self, request, *args, **kwargs):
        self.this_user = get_object_or_404(
            User,
            pk=kwargs.get('pk'),
        )
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        if self.this_user:
            relation = Relation.objects.filter(
                from_user=request.user,
                to=self.this_user,
            )

            if relation.exists():
                relation.delete()
                self.this_user.min_followers_count()

                request.user.min_following_count()

                level = messages.SUCCESS
                message = UsersMessages.unfollow_successfully
            else:
                level = messages.ERROR
                message = UsersMessages.unfollow_exists
        else:
            level = messages.ERROR
            message = UsersMessages.unfollow_failed

        messages.add_message(
            request,
            level=level,
            message=message,
        )
        return redirect(
            'user:user_detail',
            pk=kwargs.get('pk'),
        )
