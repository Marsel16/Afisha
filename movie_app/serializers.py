from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "id name movie_counts".split()

class DirectorCreateValidators(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=3, max_length=300)

class DirectorDetailCreateValidator(DirectorCreateValidators):
    pass

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
class MovieCreateValidators(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=300)
    description = serializers.CharField(min_length=3)
    duration = serializers.DurationField(min_value=3)
    director_id = serializers.IntegerField(min_value=1)

class MovieDetailCreateValidator(MovieCreateValidators):
    pass

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "text movie stars".split()
class ReviewCreateValidators(serializers.Serializer):
    text = serializers.CharField(min_length=3, max_length=300)
    movie_id = serializers.IntegerField(min_value=1)

class ReviewDetailCreateValidator(ReviewCreateValidators):
    pass

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

