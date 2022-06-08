from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('genre/', views.genre, name='genre'),
    path('movie/', views.movie, name='movie'),
    path('actor/', views.actor, name='actor') ]
