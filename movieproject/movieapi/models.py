from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, default="Untitled")
    genre = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(default=1900)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

