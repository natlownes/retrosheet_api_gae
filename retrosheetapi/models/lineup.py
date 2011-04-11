from django.db import models
from retrosheetapi.models.team import Team
from retrosheetapi.models.game_participant import GameParticipant

class Lineup(models.Model):
  game_participant = models.ForeignKey(GameParticipant)
  team = models.ForeignKey(Team)
  date = models.DateField(null=True)

