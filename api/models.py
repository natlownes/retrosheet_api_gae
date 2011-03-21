from django.db import models

class Team(models.Model):
  team_abbreviation = models.CharField(max_length=50) 
  league            = models.CharField(max_length=50)
  city              = models.CharField(max_length=200)
  nickname          = models.CharField(max_length=200)
  year_first_active   = models.CharField(max_length=4)
  year_last_active    = models.CharField(max_length=4)

class Player(models.Model):
  first_name = models.CharField()
  last_name  = models.CharField()
  retrosheet_id = models.CharField()
  debut_date = models.DateField()
