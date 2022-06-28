from django.db import models
from django.contrib.auth.models import User

from accounts.models import Profile


class TournamentType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    type = models.ForeignKey(TournamentType, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    date = models.DateTimeField()
    num_players = models.IntegerField()
    players = models.ManyToManyField(Profile)
