from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Melodrama', 'Melodrama'),
        ('Comedy', 'Comedy'),
        ('Action', 'Action'),
    ]
    
    movie_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    duration = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.movie_name

class Cinema(models.Model):
    cinema_name = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    seat_count = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.cinema_name

class MovieScreening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    start_date = models.DateField()
    screening_days = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie} at {self.cinema} on {self.start_date}"
