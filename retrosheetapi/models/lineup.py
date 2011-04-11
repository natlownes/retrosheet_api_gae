from django.db import models
from retrosheetapi.models.team import Team
from retrosheetapi.models.game_participant import GameParticipant

class Lineup(models.Model):
  game_participant = models.ForeignKey(GameParticipant)
  team = models.ForeignKey(Team)
  date = models.DateField(null=True)

  def to_string(self):
    return "\n".join(map((lambda lineup_entry: lineup_entry.to_string() ), self.lineupentry_set.all()))
