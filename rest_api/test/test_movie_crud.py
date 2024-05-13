import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from rest_api.models import Movies
from model_bakery import baker
from rest_api.serializers import CreatMovieRequestValidationSerializer, MoviesSerializer, MovieDetailedViewInputValidationSerializer, UpdateMovieRequestValidationSerializer
from unittest.mock import patch


class TestMovieModel(APITestCase):

    def setUp(self) -> None:
        # self.movie_created = baker.make(Movies)
        # self.movie_created = baker.make(Movies)
        self.movies = baker.make(Movies, _quantity=5)  # create 5 movie objects

    def test_movies_model_exists(self):
        movie_obj = Movies.objects.count()
        self.assertEqual(movie_obj, 5)

    def test_get_all_movies_view(self):
        url = reverse("get_all_movies")
        client = APIClient()
        response = client.get(url)

        # Serialize the movies
        serialized_movies = MoviesSerializer(self.movies, many=True).data

        # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("movies_serializer", response.data)
        self.assertEqual(response.data["movies_serializer"], serialized_movies)
        self.assertEqual(response.data["message"], "Fetched all Movies !")
        # Check the count of movies returned in the response
        self.assertEqual(len(response.data["movies_serializer"]), len(self.movies))

    def test_moive_detail_view(self):
        movie_created = baker.make(Movies)
        url = reverse("movie_detail_view")
        client = APIClient()

        # Input validation
        input_parameters = {'movie_id': movie_created.id}
        input_data = MovieDetailedViewInputValidationSerializer(data=input_parameters)
        
        self.assertTrue(input_data.is_valid(),'Input is not valid')


        response = client.post(url, input_parameters)

        # Serialize the movie object
        serialized_movie = MoviesSerializer(movie_created).data

        # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("movie_details", response.data)
        self.assertEqual(response.data["movie_details"], serialized_movie)
        self.assertEqual(response.data["message"], "Fetched Movie !")

    def test_movie_update_view(self):
        movie_created = baker.make(Movies)
        update_url = reverse("update_movie")
        client = APIClient()
        input_parameters = {"movie_id": movie_created.id, "producer": "jalsa"}
        validation_input = UpdateMovieRequestValidationSerializer(data=input_parameters)

        self.assertTrue(validation_input.is_valid(), 'Input validation Failed')

        response = client.put(update_url, input_parameters)

        # Update the movie object
        movie_created.refresh_from_db()
        movie_created.producer = "jalsa"
        serialized_movie = MoviesSerializer(movie_created).data

        # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("updated_movie_details", response.data)
        self.assertEqual(response.data["updated_movie_details"], serialized_movie)
        self.assertEqual(response.data["message"], "Updated Movie details !")

    def test_movie_create_view(self):
        create_url = reverse("create_movie")
        client = APIClient()
        create_movie_data = {
            "name": "tillu square",
            "lead_actor": "siddu jonnalagadda",
            "director": "some director",
            "producer": "Naga Vamsi",
        }

        # validating input
        validated_input = CreatMovieRequestValidationSerializer(data=create_movie_data)
        self.assertTrue(validated_input.is_valid(), 'Input validation failed in serializer level')

        response = client.post(create_url, create_movie_data)
        self.assertIn("movie_created", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_movie_data_from_response = response.data["movie_created"]
        # Check if the response data matches the data sent in the request
        self.assertEqual(
            created_movie_data_from_response["name"], create_movie_data["name"]
        )
        self.assertEqual(
            created_movie_data_from_response["lead_actor"],
            create_movie_data["lead_actor"],
        )
        self.assertEqual(
            created_movie_data_from_response["director"], create_movie_data["director"]
        )
        self.assertEqual(
            created_movie_data_from_response["producer"], create_movie_data["producer"]
        )


# serializer input validation
# Token , JWT, session authentication testing
