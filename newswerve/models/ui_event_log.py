
from django.db import models
from django.contrib.auth.models import User
from .skier_info import skier_info

class ui_event_log(models.Model):
    user = models.ForeignKey(skier_info, on_delete=models.SET_NULL, null=True)
    event_type = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
