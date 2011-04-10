from django.db import models

class Lineup(models.Model):
  game = models.ForeignKey(GameParticipant)
  team = models.ForeignKey(Team)
  date = models.DateField(null=True)

