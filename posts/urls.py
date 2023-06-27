from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'posts'
urlpatterns = [
    path(
        '',
        views.explore_view,
        name='explore',
    ),
    path(
        'tags/<str:tag_name>/',
        views.tag_posts_view,
        name='tag_posts',
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
