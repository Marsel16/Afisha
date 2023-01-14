from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer,\
    DirectorCreateValidators, MovieCreateValidators, ReviewCreateValidators, DirectorDetailCreateValidator,\
    MovieDetailCreateValidator, ReviewDetailCreateValidator
from rest_framework import status


@api_view(["GET", "POST"])
def directors_view(request):
    print(request.user)
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializer(instance=directors, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        serializer = DirectorCreateValidators(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get("name")
        director = Director.objects.create(name=name)
        return Response(data={"director": DirectorSerializer(director).data})


@api_view(["GET", "PUT", "DELETE"])
def director_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs["id"])
    except Director.DoesNotExist:
        return Response(data={"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        director.name = request.data.get('name')
        return Response(data={"director": DirectorSerializer(director).data})
    else:
        serializer = DirectorDetailCreateValidator(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        director.save()
        return Response(data={'message': 'data received!',
                              'movie': DirectorSerializer(director).data})

@api_view(["GET", "POST"])
def movies_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        serializer = MovieCreateValidators(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director = serializer.validated_data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director=director)
        return Response(data={"movie": MovieSerializer(movie).data})


@api_view(["GET", "PUT", "DELETE"])
def movie_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs["id"])
    except Movie.DoesNotExist:
        return Response(data={"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director')
        return Response(data={"movie": MovieSerializer(movie).data})
    else:
        serializer = MovieDetailCreateValidator(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        movie.save()
        return Response(data={'message': 'data received!',
                              'movie': MovieSerializer(movie).data})

@api_view(["GET", "POST"])
def reviews_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        serializer = ReviewCreateValidators(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        movie = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')
        review = Review.objects.create(text=text, movie=movie, stars=stars)
        return Response(data={"review": ReviewSerializer(review).data})


@api_view(["GET", "PUT", "DELETE"])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs["id"])
    except Review.DoesNotExist:
        return Response(data={"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie')
        review.stars = request.data.get('stars')
        return Response(data={"review": ReviewSerializer(review).data})
    else:
        serializer = ReviewDetailCreateValidator(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        review.save()
        return Response(data={'message': 'data received!',
                              'movie': MovieSerializer(review).data})




@api_view(["GET"])
def movies_reviews_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
