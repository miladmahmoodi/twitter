from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path(
        '<str:username>/',
        views.user_detail,
        name='user_detail',

    ),
    path(
        '<str:username>/status/<uuid:post_id>/',
        views.post_detail,
        app_name='post_detail',
    )
]
