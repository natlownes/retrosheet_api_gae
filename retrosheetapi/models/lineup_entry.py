from django.db import models
from retrosheetapi.models.lineup import Lineup
from retrosheetapi.models.player import Player

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

  @classmethod
  def defensive_position_to_name(cls, integer):
    return cls.DEFENSIVE_CHOICES[int(integer) - 1][1]

  def to_string(self):
    return "%(batting_position)02d.  %(player_name)s  %(fielding_name)s" % {'batting_position': self.batting_position, 'player_name': self.player.name(), 'fielding_name': LineupEntry.defensive_position_to_name(self.defensive_position)}

