from django.http import HttpResponse
from re import template
from multiprocessing import context
from django.shortcuts import render
from django.template import loader



from .models import Genre, Movie, Actor


def index(request):   
    index_list = 'Genre', 'Actor', 'Movie'
    template = loader.get_template('movies/index.html')
    context = {'index_list': index_list}
    return HttpResponse(template.render(context, request))
    

def genre(request):
    genre_list = Genre.objects.all
    template = loader.get_template('movies/genre.html')
    context = {'genre_list':genre_list}
    return HttpResponse(template.render(context, request))


def movie(request):
    movie_list = Movie.objects.all
    template = loader.get_template('movies/movie.html')
    context = {'movie_list':movie_list}
    return HttpResponse(template.render(context, request))

def actor(request):
    actor_list = Actor.objects.all
    template = loader.get_template('movies/actor.html')
    context = {'actor_list':actor_list}
    return HttpResponse(template.render(context, request))
