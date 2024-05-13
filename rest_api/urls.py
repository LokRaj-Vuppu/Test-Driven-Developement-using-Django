from django.urls import path
from rest_api import views as rest_api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("get_all_movies/", rest_api_views.get_all_movies, name="get_all_movies"),
    path("movie_detail_view/", rest_api_views.movie_detail_view, name="movie_detail_view"),
    path("update_movie/", rest_api_views.update_movie, name="update_movie"),
    path("create_movie/", rest_api_views.create_movie, name="create_movie"),
    path("input_validation_with_serializer/",rest_api_views.input_validation_with_serializer,
        name="input_validation_with_serializer",
    ),
    # session authentication using CSRFToken
    path('api_login_session_auth/', rest_api_views.api_login_session_auth, 
                        name='api_login_session_auth'),
    # Token Authentication using generated Token
    path('api_login_token_auth/', rest_api_views.CustomAuthToken.as_view(), name='api_login_token_auth'),
    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
