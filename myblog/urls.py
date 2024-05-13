from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("posts.urls"), name="posts"),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("api/", include("rest_api.urls")),
]
