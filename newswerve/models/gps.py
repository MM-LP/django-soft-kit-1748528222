
from django.db import models
from django.contrib.auth.models import User

class gps(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    heading = models.FloatField(null=True, blank=True)
    correction_source = models.CharField(max_length=100, null=True, blank=True)
    rtk_receiver_provider = models.CharField(max_length=100, null=True, blank=True)
    base_station_lat = models.FloatField(null=True, blank=True)
    base_station_lng = models.FloatField(null=True, blank=True)
    base_station_height = models.FloatField(null=True, blank=True)
    surveyed_in = models.BooleanField(default=False)
    ntrip_username = models.CharField(max_length=100, blank=True, null=True)
