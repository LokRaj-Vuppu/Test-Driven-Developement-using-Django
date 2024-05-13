from model_bakery import baker
from rest_api.models import Movies


def run():
    baker.make(Movies, _quantity=5)  # create 5 movie objects
