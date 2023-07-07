from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login

from users.models import User
from users.forms import RegisterForm
from core.utils import UsersMessages


class SignupView(View):
    template_name = 'users/register.html'
    form_class = RegisterForm

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
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            login(
                request,
                user,
            )
            messages.add_message(
                request,
                level=messages.SUCCESS,
                message=UsersMessages.register_successfully,
            )
            return redirect(
                'user:user_detail',
                pk=user.pk,
            )
        messages.add_message(
            request,
            level=messages.ERROR,
            message=UsersMessages.register_failed,
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
