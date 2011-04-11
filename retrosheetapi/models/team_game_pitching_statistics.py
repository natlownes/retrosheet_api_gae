from django.db import models
from retrosheetapi.models.game_participant import GameParticipant

class TeamGamePitchingStatistics(models.Model):
  pitchers_used_count = models.IntegerField(null=True)
  individual_earned_runs = models.IntegerField(null=True)
  team_earned_runs = models.IntegerField(null=True)
  wild_pitch_count = models.IntegerField(null=True)
  balk_count = models.IntegerField(null=True)
  game_participant = models.ForeignKey(GameParticipant)
