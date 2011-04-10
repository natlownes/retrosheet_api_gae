from django.db import models
from api.models.player import Player

class Game(models.Model):
  attendance = models.IntegerField(null=True)
  day_of_week = models.CharField(null=True)
  date = models.DateField(null=True)
  duration_in_minutes = models.IntegerField(null=True)
  winning_pitcher = models.ForeignKey(Player)
  losing_pitcher = models.ForeignKey(Player)

