from django.db import models

class Player(models.Model):
  first_name = models.CharField(max_length=255)
  last_name  = models.CharField(max_length=255)
  retrosheet_id = models.CharField(max_length=255)
  debut_date = models.DateField(null=True)
  #debut_year = models.IntegerField()
  #debut_month = models.IntegerField()
  #debut_day = models.IntegerField()

  @classmethod
  def destroy_all(cls):
    # I know there's gotta be a better way to do this
    for player in Player.objects.all():
      player.delete()


