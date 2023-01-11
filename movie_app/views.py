from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework import status
@api_view(["GET"])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def director_detail_view(request, **kwargs):
    director = Director.objects.get(id=kwargs["id"])
    serializer = DirectorSerializer(director, many=False)
    return Response(data=serializer.data)


@api_view(["GET"])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(["GET"])
def movie_detail_view(request, **kwargs):
    movie = Movie.objects.get(id=kwargs["id"])
    serializer = MovieSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(["GET"])
def reviews_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

@api_view(["GET"])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs["id"])
    except Review.DoesNotExist:
        return Response(data={"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def movies_reviews_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
