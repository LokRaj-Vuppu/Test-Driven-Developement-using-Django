from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthenticationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="test_user", password="password123"
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)

    # login and getting access and refresh token
    def test_jwt_authentication(self):
        url = reverse("token_obtain_pair")
        data = {"username": "test_user", "password": "password123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")
        # adding token in header while sending request to API

        movie_response = self.client.get(reverse("get_all_movies"))

        self.assertEqual(movie_response.status_code, status.HTTP_200_OK)

    # for failure cases
    def test_jwt_authentication_failure(self):
        url = reverse("token_obtain_pair")
        data = {"username": "test_user", "password": "wrong_password"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # to get the new access token after generating new refresh token
    def test_refresh_token(self):
        url = reverse("token_refresh")
        refresh_token = RefreshToken.for_user(self.user)
        data = {"refresh": str(refresh_token)}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
