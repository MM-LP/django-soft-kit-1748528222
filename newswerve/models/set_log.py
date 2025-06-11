from django.db import models
from .skier_info import skier_info
from .course import course
from .boat_info import boat_info
from .driver_info import driver_info
from .log import log

class set_log(models.Model):
    skier = models.ForeignKey(skier_info, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.SET_NULL, null=True)
    boat = models.ForeignKey(boat_info, on_delete=models.SET_NULL, null=True)
    boat_driver = models.ForeignKey(driver_info, on_delete=models.SET_NULL, null=True)
    coach = models.CharField(max_length=255, null=True, blank=True)
    log = models.ForeignKey(log, on_delete=models.SET_NULL, null=True)
    session_number = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
