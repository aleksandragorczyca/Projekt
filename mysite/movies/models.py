from django.db import models



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
    description = models.TextField()

    def __str__(self):
        return self.movie_name


