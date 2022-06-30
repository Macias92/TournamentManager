from django.db import models
from django.contrib.auth.models import User


class TournamentType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=256)


class Player(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(TournamentType, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    date = models.DateField()
    time = models.TimeField(null=True)
    num_players = models.PositiveIntegerField()


class Match(models.Model):
    teams = models.ManyToManyField(Team)
    team1_result = models.PositiveIntegerField()
    team2_result = models.PositiveIntegerField()
    win_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winners')
    lose_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='losers')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)


class Game(models.Model):
    name = models.CharField(max_length=32)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

