from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя режиссера")
    @property
    def movie_counts(self):
        return self.movie_set.all().count()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    duration = models.DurationField(verbose_name="Длительность")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name="Режиссер")

    @property
    def rating(self):
        sum_stars = sum([review.stars for review in self.reviews.all()])
        reviews_count = self.reviews.all().count()
        if reviews_count > 0:
            return sum_stars / reviews_count
        else:
            return 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Review(models.Model):
    text = models.TextField(verbose_name="Отзыв")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм", related_name="reviews")
    stars = models.IntegerField(verbose_name="Оценка", choices=((i, i * "*") for i in range(1, 6)))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
