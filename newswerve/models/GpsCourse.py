from django.db import models

class GpsCourse(models.Model):
    coordinate_source = models.CharField(max_length=255, blank=True, null=True)


