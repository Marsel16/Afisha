# Generated by Django 4.1.4 on 2022-12-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_director_options_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(verbose_name='Длительность'),
        ),
    ]
