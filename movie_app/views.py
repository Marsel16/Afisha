from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

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
    print(serializer.data)
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
    review = Review.objects.get(id=kwargs["id"])
    serializer = ReviewSerializer(review, many=False)
    return Response(data=serializer.data)
