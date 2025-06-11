from django.db import models

class gps_course(models.Model):
    coordinate_source = models.CharField(max_length=255, blank=True, null=True)


