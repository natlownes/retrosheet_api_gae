from django.db import models
from api.models.team import Team
from api.models.game_participant import GameParticipant

class Lineup(models.Model):
  game = models.ForeignKey(GameParticipant)
  team = models.ForeignKey(Team)
  date = models.DateField(null=True)

