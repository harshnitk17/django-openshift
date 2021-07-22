from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.fields import CharField
 
class Parameters(models.Model):
    data = JSONField()

class user_plots(models.Model):
    img_path=models.CharField(max_length=2000)
    img_id=models.UUIDField()
