from django.db import models

class TeamGameDefenseStatistics(models.Model):
  putouts_count = models.IntegerField(null=True)

