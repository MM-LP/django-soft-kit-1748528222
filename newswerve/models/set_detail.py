from django.db import models

class set_detail(models.Model):
    session_number = models.IntegerField(blank=True, null=True)
    pass_number = models.IntegerField(blank=True, null=True)
    pass_time = models.DateTimeField(blank=True, null=True)
    rope_length = models.IntegerField(blank=True, null=True)
    pass_speed = models.IntegerField(blank=True, null=True)
    zero_off = models.IntegerField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    personal_best = models.BooleanField(default=False)
    pb_term = models.CharField(max_length=255, blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    as_mode = models.BooleanField(blank=False)
    competition = models.IntegerField(null=True, blank=True)
