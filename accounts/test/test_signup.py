from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegistrationForm
from django.contrib.auth import get_user_model


User = get_user_model()


# Test account registration
class AccountCreationTest(TestCase):
    def setUp(self) -> None:
        self.form_class = UserRegistrationForm

    # test if registration template is being rendered
    def test_signup_page_exists(self):
        response = self.client.get(reverse("signup_page"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "accounts/register.html")
        # self.assertContains(response, "Create Your Account Today !")

    # test for all form fields are displaying in template, form validation by submitting sample from
    def test_user_registration_form_works_correctly(self):

        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue("email" in self.form_class.Meta.fields)
        self.assertTrue("username" in self.form_class.Meta.fields)
        self.assertTrue("password1" in self.form_class.Meta.fields)
        self.assertTrue("password2" in self.form_class.Meta.fields)

        input_form_data = {
            "email": "test@app.com",
            "username": "testuser",
            "password1": "Pass@12345",
            "password2": "Pass@12345",
        }

        form = self.form_class(input_form_data)

        self.assertTrue(form.is_valid())

    def test_signup_form_creates_user_in_db(self):
        user = {
            "email": "test1@app.com",
            "username": "testuser1",
            "password1": "Pass@12345",
            "password2": "Pass@12345",
        }

        form = self.form_class(user)

        if form.is_valid():
            form.save()

        self.assertTrue(User.objects.get(email=user["email"]))
        self.assertEqual(User.objects.count(), 1)
