from django.contrib import admin
from .models import Movie, Cinema, MovieScreening

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'genre', 'duration', 'rating')
    search_fields = ('movie_name',)

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('cinema_name', 'ticket_price', 'seat_count', 'address', 'phone_number')
    search_fields = ('cinema_name',)

@admin.register(MovieScreening)
class MovieScreeningAdmin(admin.ModelAdmin):
    list_display = ('movie', 'cinema', 'start_date', 'screening_days')
    search_fields = ('movie__movie_name', 'cinema__cinema_name')
