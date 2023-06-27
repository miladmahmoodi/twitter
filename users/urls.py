from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'users'
urlpatterns = [
    path(
      'signin/',
      views.signin_view,
      name='signin',
    ),
    path(
      'signout/',
      views.signout_view,
      name='signout',
    ),
    path(
        'home/',
        views.home_view,
        name='home',

    ),
    path(
      'follow/<str:username>/',
      views.follow_view,
      name='follow',
    ),
    path(
      'unfollow/<str:username>/',
      views.unfollow_view,
      name='unfollow',
    ),
    path(
        '<str:username>/',
        views.user_detail_view,
        name='user_detail',
    ),
    path(
      '<str:username>/archive/',
      views.user_archive_view,
      name='user_archive',
    ),
    path(
        '<str:username>/status/<uuid:post_id>/',
        views.post_detail_view,
        name='post_detail',
    ),
    path(
      '<str:username>/status/<uuid:post_id>/archive/',
      views.post_archive_view,
      name='post_archive',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

