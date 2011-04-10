from django.db import models
from api.models.game import Game
from api.models.team import Team
from api.models.player import Player

# a team that has participated in a game
class GameParticipant(models.Model):
  HOME_OR_AWAY_CHOICES = (
      (u'home', u'Home'),
      (u'away', u'Away')
  )
  game = models.ForeignKey(Game)
  team = models.ForeignKey(Team)
  starting_pitcher = models.ForeignKey(Player)

  game_number_for_season = models.IntegerField(null=True)
  team_location_status = models.CharField(choices=HOME_OR_AWAY_CHOICES)
  runs_scored_count = models.IntegerField(null=True)
