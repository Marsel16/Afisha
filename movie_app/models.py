from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя режиссера")

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Review(models.Model):
    text = models.TextField(verbose_name="Отзыв")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return self.text
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"