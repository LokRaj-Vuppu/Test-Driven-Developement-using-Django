from model_bakery import baker
from rest_api.models import Movies, Book
from faker import Faker
import random
faker = Faker()


def run():
    # baker.make(Movies, _quantity=5)  # create 5 movie objects
    # book_create_list = []
    # for i in range(1, 5000):
    #     book = Book(title=faker.name(), author=faker.company(), publication_date=faker.date())
    #     book_create_list.append(book)


    # Book.objects.bulk_create(book_create_list)

    movie_create_list = []
    for i in range(1, 5000):
        movie = Movies(name=faker.name(), lead_actor=faker.last_name(), director=faker.first_name(),
                       producer=faker.first_name_nonbinary(), banner=faker.suffix(), distributor=faker.bs(), 
                       release_date=faker.date(), rating=float("{0:.1f}".format(random.uniform(4, 9.8)))
        )
        movie_create_list.append(movie)

    Movies.objects.bulk_create(movie_create_list)
