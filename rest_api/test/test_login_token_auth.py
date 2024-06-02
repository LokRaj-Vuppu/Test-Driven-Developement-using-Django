from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

# commented session authentication and added Token authentication in setting.py filr


class TestTokenAuth(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.username, self.password, self.email = (
            "testuser",
            "testpassword",
            "testuser@gmail.com",
        )
        self.user = User.objects.create_user(
            username=self.username, password=self.password, email=self.email
        )
        self.get_all_movies = reverse("get_all_movies")
        self.token_login_url = reverse("api_login_token_auth")
        self.login_input = {"username": self.username, "password": self.password}
        self.login_response = self.client.post(self.token_login_url, self.login_input)

    def test_get_all_movies_protected_view(self):

        self.assertEqual(self.login_response.status_code, status.HTTP_200_OK)
        self.assertIn("token", self.login_response.data)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.login_response.data['token']}"
        )

        movie_response = self.client.get(self.get_all_movies)  # protected view
        self.assertEqual(
            movie_response.status_code,
            status.HTTP_200_OK,
            "error in get_all_movies API",
        )
