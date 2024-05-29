from rest_framework import serializers
from rest_api.models import Movies, Book
from posts.models import Post


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = "__all__"


class InputValidationserializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    age = serializers.IntegerField(min_value=20)
    city = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    state = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    country = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    mobile = serializers.CharField(required=True, allow_null=False, allow_blank=False)


class MovieDetailedViewInputValidationSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField(required=True, allow_null=False)


class UpdateMovieRequestValidationSerializer(serializers.Serializer):
    producer = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    movie_id = serializers.IntegerField(required=True, allow_null=False)


class CreatMovieRequestValidationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    lead_actor = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    director = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    producer = serializers.CharField(required=True, allow_null=False, allow_blank=False)


class LoginRequestValidationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'