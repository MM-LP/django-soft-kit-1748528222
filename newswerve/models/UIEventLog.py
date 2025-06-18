
from django.db import models
from django.contrib.auth.models import User
from .UserPreferences import UserPreferences
from django.utils import timezone

class UIEventLog(models.Model):
    user_id = models.ForeignKey(UserPreferences, on_delete=models.SET_NULL, null=True)
    event_type = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
