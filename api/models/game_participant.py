from django.db import models

# a team that has participated in a game
class GameParticipant(models.Model):
  HOME_OR_AWAY_CHOICES = (
      (u'home', u'Home'),
      (u'away', u'Away')
  )
  game = models.ForeignKey(Game)
  team = models.ForeignKey(Team)
  game_number_for_season = models.IntegerField(null=True)
  team_location_status = models.CharField(choices=HOME_OR_AWAY_CHOICES)
