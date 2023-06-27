from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from posts.models import Post, Comment
from users.models import User


def post_archive_view(request, username, post_id):

    if request.method == 'GET':
        post = get_object_or_404(
            Post,
            id=post_id,
        )
        if request.user == post.user:
            post.delete()

        return redirect(
            f'/{post.user}/'
        )
