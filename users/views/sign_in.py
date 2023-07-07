from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from users.forms import SigninForm
from core.utils import UsersMessages


class SigninView(View):
    template_name = 'users/sign-in.html'
    form_class = SigninForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(
                'user:home',
            )
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user:
                login(
                    request,
                    user,
                )
                messages.add_message(
                    request,
                    level=messages.SUCCESS,
                    message=UsersMessages.login_successfully
                )
                return redirect(
                    'user:user_detail',
                    pk=user.pk,
                )
            messages.error(
                request,
                message=UsersMessages.login_fail,
            )
        context = {
            'form': form,
        }
        return render(
            request,
            template_name=self.template_name,
            context=context,
            status=400,
        )
