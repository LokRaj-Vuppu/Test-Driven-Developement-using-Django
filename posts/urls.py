from django.urls import path
from posts import views as posts_views


urlpatterns = [
    path("", posts_views.index, name="homepage"),
    path("post/<int:id>/", posts_views.post_detail, name="post_detail"),
    path("create_post/", posts_views.create_post, name="create_post"),
]

generic_class_based_views_django = [
    path(
        "posts_list_view/", posts_views.PostsListView.as_view(), name="posts_list_view"
    ),
    path(
        "posts_detail_view/<int:pk>/",
        posts_views.PostsDetailView.as_view(),
        name="posts_detail_view",
    ),
    path(
        "create_post_view/",
        posts_views.PostCreationView.as_view(),
        name="create_post_view",
    ),
    path(
        "update_post_view/<int:pk>/",
        posts_views.PostUpdationView.as_view(),
        name="update_post_view",
    ),
    path(
        "delete_post_view/<int:pk>/",
        posts_views.PostDeleteView.as_view(),
        name="delete_post_view",
    ),
    path("post_created/", posts_views.post_created, name="post_created"),
    path("post_updated/", posts_views.post_updated, name="post_updated"),
    path("post_deleted/", posts_views.post_updated, name="post_deleted"),
]

urlpatterns += generic_class_based_views_django
