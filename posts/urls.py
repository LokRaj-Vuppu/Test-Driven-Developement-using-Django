from django.urls import path
from posts import views as posts_views


urlpatterns = [
    path("", posts_views.index, name="homepage"),
    path("post/<int:id>/", posts_views.post_detail, name="post_detail"),
    path("create_post/", posts_views.create_post, name="create_post"),
]
