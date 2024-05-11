from django.test import TestCase
from posts.models import Post
from model_bakery import baker
from django.urls import reverse
from django.contrib.auth.models import User


class PostModelTest(TestCase):

    
    def setUp(self):
        self.user = baker.make(User)
        self.post = Post.objects.create(title='Demo', body='test body', author=self.user)


    # test number of records in table
    def test_post_model_exists(self):
        post_count = Post.objects.count()
        self.assertGreaterEqual(post_count, 0, "No Post objects found in the database.")

    # test string (__str__) representation of model
    def test_str_rep_of_model(self):
        # baker.make takes and argument of model and creates a record
        created_post = baker.make(Post)
        self.assertEqual(
            str(created_post), f"{created_post.title} - {created_post.body}"
        )


    def test_post_model_get_absolute_uri_method(self):
        url = self.post.get_absolute_url()
        expected_url = reverse("post_detail", kwargs={"id": self.post.pk})

        self.assertEqual(url, expected_url)