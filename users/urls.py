from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

