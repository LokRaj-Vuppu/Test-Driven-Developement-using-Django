from django.test import TestCase
from posts.models import Post
from http import HTTPStatus
from model_bakery import baker


class HomePageTest(TestCase):
    # setup() runs during the class initialization
    def setUp(self):
        self.post1 = baker.make(Post)  # baker will create an object
        self.post1 = baker.make(Post)

    # test if home page renders index.html template and status code is 200
    def test_home_page_renders_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/index.html")

    # test if home page contains post's title
    def test_home_page_contains_post(self):
        response = self.client.get("/")
        self.assertContains(response, self.post1.title)
