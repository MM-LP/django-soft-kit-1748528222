from django.db import models
from .UserPreferences import UserPreferences
from django.utils import timezone

class MediaLayoutPreset(models.Model):
    user_id = models.ForeignKey(UserPreferences, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    json_layout = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
