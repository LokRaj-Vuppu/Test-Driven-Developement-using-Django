from django.test import TestCase
from django.contrib.auth import get_user_model
from model_bakery import baker
from faker import Faker
from posts.models import Post


User = get_user_model()
fake = Faker()


class PostAuthorTest(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.post = Post.objects.create(
            title=fake.name(), body=fake.text(), author=self.user
        )

    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))

    def test_post_belongs_to_user(self):
        self.assertTrue(hasattr(self.post, "author"))
        self.assertEqual(self.post.author, self.user)
