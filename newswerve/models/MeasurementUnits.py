from django.db import models
from django.utils import timezone

class MeasurementUnits(models.Model):
    system = models.CharField(max_length=15, null=True, blank=True)
    activity = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    unit = models.CharField(max_length=20, null=True, blank=True)
    symbol = models.CharField(max_length=20, null=True, blank=True)
    value = models.CharField(max_length=20, null=True, blank=True)
    system_alt = models.CharField(max_length=20, null=True, blank=True)
    system_convert = models.FloatField()
