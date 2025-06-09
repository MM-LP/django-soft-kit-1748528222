
from django.db import models

class CourseSurveyData(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    survey_date = models.DateField(blank=True, null=True)
    survey_tool = models.CharField(max_length=100, blank=True, null=True)
    correction_type = models.CharField(max_length=100, blank=True, null=True)
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

class ASOperation(models.Model):
    ff = models.IntegerField(blank=True, null=True)
    pgain = models.IntegerField(blank=True, null=True)
    igain = models.IntegerField(blank=True, null=True)
    dgain = models.IntegerField(blank=True, null=True)
    st_target = models.IntegerField(blank=True, null=True)
    st_actual = models.IntegerField(blank=True, null=True)
    rudder_position = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

class Autosteer(models.Model):
    boat = models.ForeignKey('Boat', on_delete=models.SET_NULL, null=True)
    as_status = models.BooleanField(default=False)
    current_config = models.BooleanField(blank=False)
    auto_steer_system = models.CharField(max_length=255, blank=True, default='Standard')
    rudder_trim = models.FloatField(blank=True, null=True)
    imu_offset = models.FloatField(blank=True, null=True)
    gps_offset = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)
