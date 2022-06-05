# Generated by Django 4.0.5 on 2022-06-04 18:08

import autoslug.fields
from django.db import migrations
from django.utils.text import slugify

DEFAULT = "abc"


def forwards(apps, _):
    Movie = apps.get_model("movies", "Movie")
    movies = Movie.objects.all()
    for movie in movies:
        movie.slug = slugify(movie.title)
        movie.save()


def backwards(apps, _):
    Movie = apps.get_model("movies", "Movie")
    movies = Movie.objects.all()
    for movie in movies:
        movie.slug = DEFAULT
        movie.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_popularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(
                always_update=True, default=DEFAULT, editable=True, populate_from='title'),
            preserve_default=False,
        ),
        migrations.RunPython(forwards, backwards)
    ]