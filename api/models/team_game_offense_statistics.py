from django.db import models

class TeamGameOffenseStatistics(models.Model):
  at_bats_count = models.IntegerField(null=True)

