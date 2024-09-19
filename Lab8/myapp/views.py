from django.shortcuts import render
from .models import Movie, Cinema, MovieScreening

def home(request):
    movies = Movie.objects.all()
    cinemas = Cinema.objects.all()
    screenings = MovieScreening.objects.all()
    return render(request, 'myapp/home.html', {
        'movies': movies,
        'cinemas': cinemas,
        'screenings': screenings
    })
