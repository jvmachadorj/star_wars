from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=200)
    climate = models.CharField(max_length=200)
    terrain = models.CharField(max_length=200)
    movie_appearance = models.IntegerField()
