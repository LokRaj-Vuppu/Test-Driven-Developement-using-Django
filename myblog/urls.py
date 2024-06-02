from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("posts.urls"), name="posts"),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("api/", include("rest_api.urls")),
    path("orm/", include("aa_orm.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
