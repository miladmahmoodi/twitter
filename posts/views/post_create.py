from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages

from posts.forms import PostCreateForm, ImageCreateFormSet
from posts.models import Image, Tag
from core.utils import UsersMessages, PostTitleExists


class PostCreateView(LoginRequiredMixin, View):
    """

    """

    template_name = 'posts/create-post.html'
    form_class = PostCreateForm
    image_form_set = ImageCreateFormSet

    def get(self, request):
        """

        :param request:
        :return:
        """

        context = {
            'form': self.form_class(),
            'image_form': self.image_form_set(),
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request):
        form = self.form_class(request.POST)
        image_form = self.image_form_set(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            try:
                post = form.save(
                    commit=False,
                )
                post.user = request.user
                post.save()

                for tag in form.cleaned_data.get('tags').split(' '):
                    if tag.startswith('#'):
                        obj, created = Tag.objects.get_or_create(
                            name=tag,
                        )
                        post.tag.add(obj)

                for image in image_form.cleaned_data:
                    if image:
                        Image.objects.create(
                            name=image.get('name'),
                            alt=image.get('alt'),
                            image=image.get('image'),
                            post=post,
                        )
            except Exception as err:
                messages.add_message(
                    request,
                    level=messages.ERROR,
                    message=UsersMessages.integrity_exception,
                )
                return redirect(
                    'post:create_post',
                )

            else:
                post.user.add_post_count()

                messages.add_message(
                    request,
                    level=messages.SUCCESS,
                    message=UsersMessages.create_post_successfully,
                )
                return redirect(
                    'user:user_detail',
                    pk=request.user.pk,
                )

        context = {
            'form': self.form_class(),
            'image_form': self.image_form_set(),
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
        )
