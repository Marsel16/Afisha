from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework import status


@api_view(["GET", "POST"])
def directors_view(request):
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        name = request.data.get('name')
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


@api_view(["GET", "POST"])
def movies_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
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
        movie.director = request.data.get('director')
        return Response(data={"movie": MovieSerializer(movie).data})


@api_view(["GET", "POST"])
def reviews_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
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
        review.movie = request.data.get('movie')
        review.stars = request.data.get('stars')
        return Response(data={"review": ReviewSerializer(review).data})





@api_view(["GET"])
def movies_reviews_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
