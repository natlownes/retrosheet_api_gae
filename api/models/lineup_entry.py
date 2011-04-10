from django.db import models
from api.models.lineup import Lineup
from api.models.player import Player

class LineupEntry(models.Model):
  DEFENSIVE_CHOICES = (
      (1, u'P'),
      (2, u'C'),
      (3, u'1B'),
      (4, u'2B'),
      (5, u'3B'),
      (6, u'SS'),
      (7, u'LF'),
      (8, u'CF'),
      (9, u'RF'),
      (10, u'DH')
  )
  lineup = models.ForeignKey(Lineup)
  player = models.ForeignKey(Player)
  is_starter = models.BooleanField()
  batting_position = models.IntegerField()
  defensive_position = models.IntegerField(choices=DEFENSIVE_CHOICES)


