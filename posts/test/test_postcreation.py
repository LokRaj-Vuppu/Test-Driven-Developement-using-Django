from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from posts.forms import PostCreationForm
from django.http.request import HttpRequest
from model_bakery import baker
from django.contrib.auth import get_user_model
from posts.models import Post


User = get_user_model()


class TestPostCreation(TestCase):

    def setUp(self):
        self.url = reverse("create_post")
        self.template_name = "posts/createpost.html"
        self.form_name = PostCreationForm

        user = User.objects.create_user(
            username="teste3", password="tetT@1232", email="testmail@mailt.in"
        )

    def test_create_post_form_exists(self):
        self.client.login(username="teste3", password="tetT@1232")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)

        form = response.context.get("form", None)

        self.assertTrue(isinstance(form, self.form_name))

    def test_post_creation_form_creates_post(self):
        post_request = HttpRequest()

        post_request.user = baker.make(User)

        post_data = {"title": "Numpy", "body": "Python Library"}

        post_request.POST = post_data

        form = self.form_name(post_request.POST)
        self.assertTrue(form.is_valid())

        post_obj = form.save(commit=False)
        self.assertIsInstance(post_obj, Post)

        post_obj.author = post_request.user
        post_obj.save()

        self.assertEqual(
            post_request.user, Post.objects.get(author=post_request.user).author
        )
        self.assertEqual(Post.objects.count(), 1)

    def test_post_creation_requires_login(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, expected_url="/accounts/login/?next=/create_post/"
        )
