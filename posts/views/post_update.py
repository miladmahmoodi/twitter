from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings

import os

from posts.models import Post, Image
from posts.forms import PostCreateForm
from core.utils import UsersMessages


class PostUpdateView(LoginRequiredMixin, View):
    """

    """

    template_name = 'posts/create-post.html'
    form_class = PostCreateForm

    def setup(self, request, *args, **kwargs):
        self.this_post = get_object_or_404(
            Post,
            pk=kwargs.get('pk'),
        )
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :return:
        """
        context = {
            'form': self.form_class(
                instance=self.this_post,
            )
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST,
            instance=self.this_post,
        )
        if form.is_valid():
            post = form.save(commit=False)
            # post.user = request.user
            post.save()
            for image in request.FILES.getlist('images'):
                filename = image.name
                image_obj = Image.objects.create(
                    post=post,
                    name=request.POST.get('image_name'),
                    alt=request.POST.get('image_alt'),
                    image=image,
                )
                path = os.path.join(settings.MEDIA_ROOT, 'post/images/', f'{image_obj.pk}_{filename}')
                with open(path, 'wb+') as f:
                    for chunk in image.chunks():
                        f.write(chunk)
                image_obj.image = os.path.join('post/images/', f'{image_obj.pk}_{filename}')
                image_obj.save()
            messages.add_message(
                request,
                level=messages.SUCCESS,
                message=UsersMessages.update_post_successfully
            )
            return redirect(
                'post:post_detail',
                pk=post.pk,
            )
        else:
            form = self.form_class()

        context = {
            'form': form,
        }
        return render(
            request,
            template_name='posts/create_post.html',
            context=context,
        )
