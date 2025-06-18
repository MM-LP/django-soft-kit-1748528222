from django.db import models
from .Location import Location 
from django.utils import timezone

class CourseSurveyData(models.Model):
    course_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    course_name = models.CharField(max_length=100,  blank=True, null=True)
    survey_date = models.DateField(blank=True, null=True)
    survey_tool = models.CharField(max_length=100,  blank=True, null=True)
    correction_type = models.CharField(max_length=100,  blank=True, null=True)
    baseline_distance = models.FloatField(blank=True, null=True)
    course_direction = models.CharField(max_length=50, blank=True, null=True)
    homologation = models.CharField(max_length=100, blank=True, null=True)
    g1_lat = models.FloatField(blank=True, null=True)
    g1_lng = models.FloatField(blank=True, null=True)
    g2_lat = models.FloatField(blank=True, null=True)
    g2_lng = models.FloatField(blank=True, null=True)
    ext_lat = models.FloatField(blank=True, null=True)
    ext_lng = models.FloatField(blank=True, null=True)
    data = models.TextField(max_length=25, blank=True, null=True)
