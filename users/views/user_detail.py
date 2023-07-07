from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from users.models import User, Relation


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user-detail.html'

    def setup(self, request, *args, **kwargs):
        self.this_user = get_object_or_404(
            User,
            pk=kwargs.get('pk'),
        )
        return super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        posts = self.this_user.posts.all()
        context['posts'] = posts.filter(
            is_active=True,
        )

        is_following = Relation.objects.filter(
            from_user=self.request.user,
            to=self.this_user,
        ).exists()
        if is_following:
            context['is_following'] = is_following

        return context
