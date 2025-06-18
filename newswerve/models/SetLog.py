from django.db import models
from .UserPreferences import UserPreferences
from .Location import Location
from .BoatInfo import BoatInfo
from .DriverInfo import DriverInfo
from .Log import Log
from .Contacts import Contacts
from .Activities import Activities
from django.utils import timezone

class SetLog(models.Model):
    skier_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True)                  
    course_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    activity_id = models.ForeignKey(Activities, on_delete=models.SET_NULL, null=True)  
    boat_id = models.ForeignKey(BoatInfo, on_delete=models.SET_NULL, null=True)
    boatdriver_id = models.ForeignKey(DriverInfo, on_delete=models.SET_NULL, null=True)
    coach = models.CharField(max_length=255, null=True, blank=True)
    log_id = models.ForeignKey(Log, on_delete=models.SET_NULL, null=True)
    session_number = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(auto_now=True, null=True)
    end_time = models.DateTimeField(auto_now=True, null=True)
