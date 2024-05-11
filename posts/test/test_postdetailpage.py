from django.test import TestCase
from posts.models import Post
from model_bakery import baker
from http import HTTPStatus


class DetailPageTest(TestCase):

    def setUp(self):
        self.post = baker.make(Post)

    # detail page rendering correctly
    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")

    # detail page rendering correct response
    def test_detail_page_returns_correct_response_content(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        # self.assertContains(response, self.post.created_at) #convert datetime to string representation available in template
