from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def signin_view(request):
    """

    :param request:
    :return:
    """

    if request.method == 'GET':
        """
        """
        if request.user.is_authenticated:
            return redirect(
                '/home/'
            )

        return render(
            request,
            template_name='users/sign-in.html',
        )

    if request.method == 'POST':
        if not request.user.is_authenticated:
            user = authenticate(
                request,
                username=request.POST.get('username'),
                password=request.POST.get('password'),
            )
            if user:
                login(
                    request,
                    user,
                )
            else:
                return redirect(
                    '/signin/'
                )

            return redirect(
                f'/{user.username}',
            )
        return redirect(
            '/home/'
        )
