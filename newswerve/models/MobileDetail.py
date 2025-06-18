from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MobileDetail(models.Model):
    year = models.IntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    has_speed_sensor = models.BooleanField(default=False)
    has_microphone = models.BooleanField(default=False)
    has_video = models.BooleanField(default=False)
    has_compass = models.BooleanField(default=False)
    has_orientation = models.BooleanField(default=False)
    has_location = models.BooleanField(default=False)
    has_nfc = models.BooleanField(default=False)
    has_vibrometer = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_sound_output = models.BooleanField(default=True)
    has_air_temp_sensor = models.BooleanField(default=False)
    has_battery_test = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
