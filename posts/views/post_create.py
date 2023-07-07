from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from posts.forms import PostCreateForm, ImageCreateFormSet, ImageCreateForm


class PostCreateView(LoginRequiredMixin, View):
    """

    """

    template_name = 'posts/create-post.html'
    form_class = PostCreateForm
    image_form_class = ImageCreateFormSet

    def get(self, request):
        """

        :param request:
        :return:
        """

        inlines = (
            ImageCreateFormSet(),
        )

        form = PostCreateForm()
        form.inlines = inlines

        context = {
            'form': form,
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request):
        form = self.form_class(request.POST)
        image_formset = self.image_form_class(request.POST, request.FILES)
        if form.is_valid() and image_formset.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            image_formset.instance = post
            image_formset.save()
            return redirect('post:explore')
        return redirect('post:create_post')
