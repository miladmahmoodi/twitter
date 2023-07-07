from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'users'
urlpatterns = [
    path(
        'signin/',
        views.SigninView.as_view(),
        name='signin',
    ),
    path(
        'signout/',
        views.SignOutView.as_view(),
        name='signout',
    ),
    path(
        'signup/',
        views.SignupView.as_view(),
        name='signup',
    ),
    path(
        'home/',
        views.HomeView.as_view(),
        name='home',

    ),
    path(
        'search/',
        views.SearchUser.as_view(),
        name='search-user',
    ),
    path(
        'follow/<uuid:pk>/',
        views.FollowView.as_view(),
        name='follow',
    ),
    path(
        'unfollow/<uuid:pk>/',
        views.UnfollowView.as_view(),
        name='unfollow',
    ),
    path(
        '<uuid:pk>/',
        views.UserDetailView.as_view(),
        name='user_detail',
    ),
    path(
        '<uuid:pk>/edit/',
        views.UpdateProfileView.as_view(),
        name='edit_profile',
    ),
    path(
        'chang-password/',
        views.ChangePasswordView.as_view(),
        name='change-password',
    ),
    path(
        '<uuid:pk>/archive/',
        views.UserArchiveView.as_view(),
        name='user_archive',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

