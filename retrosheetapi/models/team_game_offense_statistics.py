from django.db import models
from retrosheetapi.models.game_participant import GameParticipant

class TeamGameOffenseStatistics(models.Model):
  COUNTS = [
      'at_bats_count',
      'hits_count',
      'doubles_count',
      'triples_count',
      'homeruns_count',
      'rbi_count',
      'sacrifice_hits_count',
      'walks_count',
      'intentional_walks_count',
      'strikeouts_count',
      'stolen_bases_count',
      'caught_stealing_count',
      'gidp_count',
      'catchers_interference_count',
      'left_on_base_count'
  ]
  for field in COUNTS:
    exec ("%(fieldname)s = models.IntegerField(null=True)" % {'fieldname': field})
    
  
  at_bats_count = models.IntegerField(null=True)
  game_participant = models.ForeignKey(GameParticipant)

