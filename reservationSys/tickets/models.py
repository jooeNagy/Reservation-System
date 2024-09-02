from django.db import models

# Create your models here.


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=20)

class Guest(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)


class Reservation(models.Model):
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name='guest', on_delete=models.CASCADE)