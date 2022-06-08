from django.db import models
from operator import mod


class Genre(models.Model):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=200)

    def __str__(self):
        return self.actor_name


class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor)
    movie_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.movie_name


class Reaction(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.reaction
