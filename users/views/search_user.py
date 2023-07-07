from django.views.generic import View
from django.shortcuts import render

from users.models import User


class SearchUser(View):
    """

    """

    def get(self, request):
        key = request.GET.get('search')

        queryset = User.objects.filter(
            username__icontains=key,
            is_active=True,
        )
        context = {
            'users': queryset,
        }
        return render(
            request,
            template_name='users/search-user.html',
            context=context
        )

