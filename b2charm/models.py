from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.fields import CharField
from datetime import datetime,timezone
import os
 
class Parameters(models.Model):
    data = JSONField()

class plot_info(models.Model):
    img_id = models.UUIDField(unique=True)
    img_path = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    def chk_expiry(self):
        deletion_time = 0.5 #in minutes
        now = datetime.now(timezone.utc)
        img_objs = plot_info.objects.all()
        for img_obj in img_objs:
            created=img_obj.created_on
            td=(now-created).total_seconds()
            if deletion_time==0:
                pass
            elif td >= (deletion_time*60):
                os.remove(img_obj.img_path)
                img_obj.delete()
