from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login, logout
from rest_api.models import Movies, Book
from posts.models import Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_api.serializers import CreatMovieRequestValidationSerializer, InputValidationserializer, LoginRequestValidationSerializer, MoviesSerializer, MovieDetailedViewInputValidationSerializer, \
UpdateMovieRequestValidationSerializer, BookSerializer, PostSerializer
from rest_framework import viewsets
from django.views.decorators.cache import cache_page
from rest_api.forms import ArticleForm, CommentForm, RegistrationForm



# For viewset and Routers

# DefaultRouter(), BaseRouter()
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()[:100]
    serializer_class = BookSerializer



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()[:100]
    serializer_class = PostSerializer


# Session Authentication
@api_view(['POST'])
def api_login_session_auth(request):
    try:
        print('request', request.data)
        request_info = LoginRequestValidationSerializer(data=request.data)
        if request_info.is_valid():
            username = request_info.validated_data['username']
            password = request_info.validated_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({'message':'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'Invalid Input', 'errors': request_info.errors},
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        print(f"Exception in login with username and password session auth - {error}")
        return Response({"message": "Something went wrong"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,)



# Token Authentication
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            print('token auth request', request.data)
            request_info = LoginRequestValidationSerializer(data=request.data)
            if request_info.is_valid():
                username = request_info.validated_data['username']
                password = request_info.validated_data['password']
                user = authenticate(username=username, password=password)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Invalid Input', 'errors': request_info.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(f'Exception in token auth - {error}')
            return Response({"message": "Something went wrong"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR,)



# JWT authentication


@api_view(["GET"])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# @cache_page(60 * 15)
def get_all_movies(request):
    try:
        print('request get all movies', request.data)
        movies = Movies.objects.all()[:100]
        movies_serializer = MoviesSerializer(movies, many=True).data
        return Response(
            {"movies_serializer": movies_serializer, "message": "Fetched all Movies !"},
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        print("error")
        return Response(
            {"error": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def movie_detail_view(request):
    try:
        print('request data', request.data)
        request_info = MovieDetailedViewInputValidationSerializer(data=request.data)
        if request_info.is_valid():
            movie_id = request_info.validated_data["movie_id"]
            print("movie_id", movie_id)
            movie = Movies.objects.get(id=movie_id)
            movie_serialized = MoviesSerializer(movie).data
            return Response(
                {"movie_details": movie_serialized, "message": "Fetched Movie !"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response({'message':'Invalid Input', 'errors': request_info.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error:
        print(f'Exception in movie_detail_view - {error}')
        return Response({'message':'Something went wrong'} ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def update_movie(request):
    try:
        print("request", request.data)
        request_info = UpdateMovieRequestValidationSerializer(data=request.data)
        if request_info.is_valid():
            producer = request_info.validated_data['producer']
            movie_id = request_info.validated_data['movie_id']
            movie = Movies.objects.get(id=movie_id)
            movie.producer = producer
            movie.save()
            movie_serialized = MoviesSerializer(movie).data
            return Response({"updated_movie_details": movie_serialized,"message": "Updated Movie details !",},
                            status=status.HTTP_200_OK,)
        else:
            return Response({'message':'Invalid Input', 'errors': request_info.errors},
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        print(f'Exception in updating movie - {error}')
        return Response({'message':'Something went wrong'} ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def create_movie(request):
    try:
        print('request ', request.data)
        request_info = CreatMovieRequestValidationSerializer(data=request.data)
        if request_info.is_valid():
            movie_created = Movies.objects.create(
                name=request_info.validated_data["name"],
                lead_actor=request_info.validated_data["lead_actor"],
                director=request_info.validated_data["director"],
                producer=request_info.validated_data["producer"],
            )
            movie_created_serialized = MoviesSerializer(movie_created).data
            return Response(
                {"movie_created": movie_created_serialized, "message": "Movie Created !"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({'message':'Invalid Input', 'errors': request_info.errors},
                            status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as error:
        print(f'Exception in creating a movie - {error}')
        return Response({'message':'Something went wrong'} ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["POST"])
def input_validation_with_serializer(request):
    try:
        print("request.data", request.data)
        request_data = InputValidationserializer(data=request.data)
        if request_data.is_valid():
            print("valid")
            return Response({"message": "good request"}, status=status.HTTP_200_OK)
        else:
            print("sez not valid", request_data.errors)
            return Response(
                {"errors": request_data.errors}, status=status.HTTP_400_BAD_REQUEST
            )
    except Exception as error:
        print(f"exception in input validation | {error}")


# Forms Testing
from django.forms import formset_factory
from rest_api.forms import GeeksForm
def form1(request):
    context ={} 
  
    # creating a formset and 5 instances of GeeksForm 
    GeeksFormSet = formset_factory(GeeksForm, extra = 5) 
    formset = GeeksFormSet()
    if request.method == 'POST':
        formset = GeeksFormSet(request.POST or None) 
        
        # print formset data if it is valid 
        if formset.is_valid(): 
            for form in formset: 
                print(form.cleaned_data) 
      
    # Add the formset to context dictionary 
    context['formset']= formset 
    return render(request, "rest_api/form1.html", context) 
