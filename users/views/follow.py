from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from core.utils import UsersMessages
from users.models import User, Relation


class FollowView(LoginRequiredMixin, View):
    """

    """

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:
        """

        user = get_object_or_404(
            User,
            pk=pk,
            is_active=True,
        )
        if user:
            relation = Relation.objects.filter(
                from_user=request.user,
                to=user,
            ).exists()

            if not relation:
                Relation.objects.create(
                    from_user=request.user,
                    to=user,
                )
                user.add_followers_count()
                request.user.add_following_count()

                level = messages.SUCCESS
                message = UsersMessages.follow_successfully
            else:
                level = messages.ERROR
                message = UsersMessages.follow_exists

        else:
            level = messages.ERROR
            message = UsersMessages.follow_failed


        messages.add_message(
            request,
            level=level,
            message=message,
        )
        return redirect(
            'user:user_detail',
            pk=pk,
        )
