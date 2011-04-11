from django.db import models
from retrosheetapi.models.game_participant import GameParticipant

class TeamGameDefenseStatistics(models.Model):
  COUNTS = [
      'putouts_count',
      'assists_count',
      'errors_count',
      'passed_balls_count',
      'double_plays_count',
      'triple_plays_count'
  ]
  for field in COUNTS:
    exec ("%(fieldname)s = models.IntegerField(null=True)" % {'fieldname': field})
    
  
  game_participant = models.ForeignKey(GameParticipant)
