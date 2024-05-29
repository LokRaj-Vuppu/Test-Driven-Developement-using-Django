from django.db import models

  
# Model Managers and Querysets

class MovieModelQuerySet(models.QuerySet):

    def get_movies_by_director(self, director):
        return self.filter(director=director)
    
    def get_top_rated_movies(self):
        return self.filter(rating__gte=8)
    
    def get_average_movies(self):
        return self.filter(rating__gte=6, rating__lte=8)
    
    def get_movies_with_rating(self, rating):
        return self.filter(rating=rating)
    

class MovieModelManager(models.Manager):

    def get_queryset(self):
        return MovieModelQuerySet(self.model, using=self._db)
    
    def get_movies_by_director(self, director):
        return self.get_queryset().get_movies_by_director(director)
    
    def get_top_rated_movies(self):
        return self.get_queryset().get_top_rated_movies()
    
    def get_average_movies(self):
        return self.get_queryset().get_average_movies()
    
    def get_movies_with_rating(self, rating):
        return self.get_queryset().get_movies_with_rating(rating)