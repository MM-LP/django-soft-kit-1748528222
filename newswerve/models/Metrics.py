from django.db import models
from .MeasurementUnits import MeasurementUnits
from django.utils import timezone

class Metrics(models.Model):
    met_name = models.CharField(max_length=50, blank=True, null=True)
    met_category = models.CharField(max_length=15, blank=True, null=True)
    met_desc = models.CharField(max_length=50, blank=True, null=True)
    met_unit_id = models.ForeignKey(MeasurementUnits, on_delete=models.SET_NULL, null=True)
    met_value = models.IntegerField(blank=True, null=True)
    