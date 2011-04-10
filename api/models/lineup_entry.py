from django.db import models

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
  lineup = model.ForeignKey(Lineup)
  is_starter = model.BooleanField()
  batting_position = model.IntegerField()
  defensive_position = model.IntegerField()(choices=DEFENSIVE_CHOICES)

