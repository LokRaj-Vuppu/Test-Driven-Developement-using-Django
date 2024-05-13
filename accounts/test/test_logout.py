from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class TestLogout(TestCase):

    def setUp(self):
        self.username = "test22"
        self.email = "test2@app.com"
        self.password = "Pass@12w344"
        # creating user
        user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password
        )

    def test_logout_view_logs_out_user(self):
        self.client.login(username=self.username, password=self.password)
        # login() provided by client
        self.assertTrue("_auth_user_id" in self.client.session)

        # checking after log out user id is available in session

        response = self.client.get(reverse("logout"))

        self.assertFalse("_auth_user_id" in self.client.session)
