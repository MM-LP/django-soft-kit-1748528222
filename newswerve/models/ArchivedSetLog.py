from django.db import models
from .ArchivedUserPreferences import ArchivedUserPreferences
from .Location import Location
from .BoatInfo import BoatInfo
from .DriverInfo import DriverInfo
from .Log import Log
from .ArchivedContacts import ArchivedContacts
from .Activities import Activities
from django.utils import timezone
from django.contrib.auth.models import User


class ArchivedSetLog(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    archive_skier_id = models.ForeignKey(ArchivedContacts, on_delete=models.SET_NULL, null=True)                  
    archive_course_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    archive_activity_id = models.ForeignKey(Activities, on_delete=models.SET_NULL, null=True)  
    boat_id = models.ForeignKey(BoatInfo, on_delete=models.SET_NULL, null=True)
    boatdriver_id = models.ForeignKey(DriverInfo, on_delete=models.SET_NULL, null=True)
    coach = models.CharField(max_length=255, null=True, blank=True)
    log_id = models.ForeignKey(Log, on_delete=models.SET_NULL, null=True)
    session_number = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(auto_now=True, null=True)
    end_time = models.DateTimeField(auto_now=True, null=True)
    archived_at = models.DateTimeField(auto_now_add=True)
