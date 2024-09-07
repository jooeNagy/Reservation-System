from django.db import models

# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=20)


    def __str__(self):
        return self.movie

class Guest(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.name


class Reservation(models.Model):
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE) 


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=100)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


