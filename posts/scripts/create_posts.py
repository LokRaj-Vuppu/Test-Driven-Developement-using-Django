from faker import Faker
from posts.models import Post

fake = Faker()


def run():
    post_objects_bulk_create_data = []
    for i in range(1, 25):
        post_objects_bulk_create_data.append(Post(title=fake.name(), body=fake.text()))

    Post.objects.bulk_create(post_objects_bulk_create_data)
