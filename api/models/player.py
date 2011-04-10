from django.db import models

class Player(models.Model):
  first_name = models.CharField()
  last_name  = models.CharField()
  retrosheet_id = models.CharField()
  debut_date = models.DateField(null=True)
  #debut_year = models.IntegerField()
  #debut_month = models.IntegerField()
  #debut_day = models.IntegerField()

  @classmethod
  def destroy_all(cls):
    # I know there's gotta be a better way to do this
    for player in Player.objects.all():
      player.delete()


