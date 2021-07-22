from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.fields import CharField
 
class Parameters(models.Model):
    data = JSONField()


