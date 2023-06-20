from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path(
        'home/',
        views.home_view,
        name='home',

    ),
    path(
        '<str:username>/',
        views.user_detail_view,
        name='user_detail',

    ),
    path(
        '<str:username>/status/<uuid:post_id>/',
        views.post_detail_view,
        name='post_detail',
    )
]
