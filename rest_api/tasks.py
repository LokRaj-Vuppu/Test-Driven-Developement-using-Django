# Create your tasks here

from rest_api.models import Movies

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Movies.objects.count()


@shared_task
def rename_widget(movie_id, name):
    m = Movies.objects.get(id=movie_id)
    m.name = name
    m.save()