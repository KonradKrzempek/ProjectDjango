from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    title = models.CharField(max_length=255)
    taken = models.BooleanField()
    description = models.CharField(max_length=40000)
    price = models.FloatField()
    picture_url = models.CharField(max_length=2083, default='')


class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


