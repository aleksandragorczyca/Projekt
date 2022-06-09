from django.shortcuts import render


from .models import Genre, Movie, Actor


def index(request):   
    index_list = 'Genre', 'Actor', 'Movie'
    context = {'index_list': index_list}
    return render(request, 'movies/index.html', context)
    

def genre(request):
    genre_list = Genre.objects.all
    context = {'genre_list': genre_list}
    return render(request, 'movies/genre.html', context)


def movie(request):
    movie_list = Movie.objects.all
    context = {'movie_list':movie_list}
    return render(request, 'movies/movie.html', context)

def actor(request):
    actor_list = Actor.objects.all
    context = {'actor_list':actor_list}
    return render(request, 'movies/actor.html',context)
