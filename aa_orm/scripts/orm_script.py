from pprint import pprint
from aa_orm.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.db import connection
import random


def run():

    staff, created = Staff.objects.get_or_create(name="admin staff")

    staff.restaurants.set(
        Restaurant.objects.all()[:10],
        through_defaults={"salary": random.randint(30_000, 60_000)},
    )

    pprint(connection.queries)
