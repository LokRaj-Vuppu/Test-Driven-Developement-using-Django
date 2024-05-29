from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_api import views as rest_api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r'books', rest_api_views.BookViewSet) #auto generating CRUD urls
router.register(r'posts', rest_api_views.PostViewSet)


# GET - /books/: List all books
# POST - /books/: Create a new book
# GET -  /books/{pk}/: Retrieve a specific book
# PUT - /books/{pk}/: Update a specific book
# DELETE  - /books/{pk}/: Delete a specific book


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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('cbv-test/', TemplateView.as_view(template_name='rest_api/cbv_home.html')),

]

# Using Router
book_router = [
        path('', include(router.urls)),
]


forms_testing = [
    path('form1/', rest_api_views.form1, name='form1')
]



urlpatterns += book_router
urlpatterns += forms_testing
