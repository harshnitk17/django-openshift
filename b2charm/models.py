from django.db import models
from django.contrib.postgres.fields import JSONField
 
class Parameters(models.Model):
    data = JSONField()
