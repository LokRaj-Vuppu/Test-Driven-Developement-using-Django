from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()


class TestSessionAuthentication(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username, self.password = "testuser", "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.get_all_movies = reverse("get_all_movies")
        self.login_url = reverse("api_login_session_auth")
        self.login_input = {"username": self.username, "password": self.password}
        self.login_response = self.client.post(self.login_url, self.login_input)
        self.csrf_token = self.client.cookies["csrftoken"].value  # Capture CSRF token

    def test_get_all_movies_protected_view(self):
        self.client.credentials(HTTP_X_CSRFTOKEN=self.csrf_token)  # optinal
        movie_response = self.client.get(self.get_all_movies)  # protected view

        self.assertEqual(
            movie_response.status_code,
            status.HTTP_200_OK,
            "error in get_all_movies API",
        )

        self.assertEqual(
            self.login_response.status_code, status.HTTP_200_OK, "error in login api"
        )
        self.assertEqual(
            self.login_response.data,
            {"message": "Login successful"},
            "Message does not match",
        )
