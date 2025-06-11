
from django.db import models
from .contacts import contacts 

class health(models.Model):
    fatigue_level = models.IntegerField(blank=True, null=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    hydration = models.IntegerField(null=True, blank=True)
    mood = models.CharField(max_length=100, blank=True, null=True)
    contact = models.ForeignKey(contacts, on_delete=models.SET_NULL, null=True)