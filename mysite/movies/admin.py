from django.contrib import admin
from .models import Genre, Movie, Actor, Reaction 

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Reaction)
