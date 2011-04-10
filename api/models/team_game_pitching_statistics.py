from django.db import models

class TeamGamePitchingStatistics(models.Model):
  pitchers_used_count = models.IntegerField(null=True)
