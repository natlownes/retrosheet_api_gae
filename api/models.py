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
  #debut_year = models.IntegerField()
  #debut_month = models.IntegerField()
  #debut_day = models.IntegerField()

  @classmethod
  def destroy_all(cls):
    # I know there's gotta be a better way to do this
    for player in Player.objects.all():
      player.delete()


