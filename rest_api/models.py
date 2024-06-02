from django.db import models
from rest_api.managers import MovieModelManager, MovieModelQuerySet


class Movies(models.Model):
    name = models.CharField(max_length=30)
    lead_actor = models.CharField(max_length=40)
    director = models.CharField(max_length=40)
    producer = models.CharField(max_length=30, null=True, blank=True)
    banner = models.CharField(max_length=100, null=True, blank=True)
    distributor = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, default=0.0
    )

    # Custom model manager
    objects = MovieModelManager()
    # objects = MovieModelQuerySet.as_manager()

    def __str__(self) -> str:
        return f"{self.name} - {self.lead_actor} - {self.director} - {self.producer}"

    class Meta:
        verbose_name_plural = "Movies"
        indexes = [models.Index(fields=["name", "lead_actor"])]


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
