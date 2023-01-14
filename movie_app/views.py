from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import *
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

class DirectorModelViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class MovieReviewListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination
