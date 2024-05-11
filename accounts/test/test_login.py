from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class TestLoginPage(TestCase):

    def setUp(self):
        self.username = "test22"
        self.email = "test2@app.com"
        self.password = "Pass@12w344"
        # creating an user
        user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password
        )

    def test_login_page_exists(self):
        response = self.client.get(reverse("login_page"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "accounts/login.html")
        self.assertContains(
            response, "Login"
        )  # checking in 'Login' word/string present in html

    def test_login_page_has_login_form(self):
        response = self.client.get(reverse("login_page"))

        form = response.context.get(
            "form"
        )  # Getting the form from the response after calling vew
        self.assertIsInstance(
            form, AuthenticationForm
        )  # checking if rendered form is same as form we created for login

    def test_login_page_logs_in_user(self):
        user_data = {"username": self.username, "password": self.password}

        response = self.client.post(
            reverse("login_page"), user_data
        )  # login with the user created in setup function

        self.assertRedirects(response, reverse("homepage"))
