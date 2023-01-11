from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "id name".split()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "text movie stars".split()

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    director = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ["title", "description", "duration", "director", "rating", "reviews"]

    def get_director(self, movie):
        return movie.director.name

    def get_reviews(self, movie):
        return [i.text for i in movie.reviews.all()]
