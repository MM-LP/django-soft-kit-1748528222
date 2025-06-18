from django.db import models
from django.utils import timezone

class Log(models.Model):
    file = models.TextField(max_length=100, blank=True, null=True)
    log_level = models.IntegerField(null=True, blank=True)
