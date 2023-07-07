from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'posts'
urlpatterns = [
    path(
        '',
        views.ExploreListView.as_view(),
        name='explore',
    ),
    path(
        'tags/<uuid:pk>/',
        views.TagPostsListView.as_view(),
        name='tag_posts',
    ),
    path(
        'posts/create/',
        views.PostCreateView.as_view(),
        name='create_post',
    ),
    path(
        'posts/<uuid:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail',
    ),
    path(
      'posts/<uuid:pk>/archive/',
      views.PostArchiveView.as_view(),
      name='post_archive',
    ),
    path(
        'posts/<uuid:pk>/edit/',
        views.PostUpdateView.as_view(),
        name='post_update',
    ),
    path(
      'posts/<uuid:pk>/like/',
      views.PostLikeView.as_view(),
      name='post_like',
    ),
    path(
      'posts/<uuid:pk>/dislike/',
      views.PostDislikeView.as_view(),
      name='post_dislike',
    ),
    path(
      'posts/<uuid:pk>/comment/<uuid:comment_pk>/reply/',
      views.CommentReplyView.as_view(),
      name='comment_reply',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
