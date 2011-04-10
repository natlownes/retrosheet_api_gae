from django.db import models

class TeamGameDefenseStatistics(models.Model):
  putouts_count = model.IntegerField(null=True)

