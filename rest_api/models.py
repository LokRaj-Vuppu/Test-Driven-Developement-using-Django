from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=30)
    lead_actor = models.CharField(max_length=40)
    director = models.CharField(max_length=40)
    producer = models.CharField(max_length=30, null=True, blank=True)
    banner = models.CharField(max_length=100, null=True, blank=True)
    distributor = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.lead_actor} - {self.director} - {self.producer}"
