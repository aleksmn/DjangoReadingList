from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    pages = models.IntegerField()
    rating = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

