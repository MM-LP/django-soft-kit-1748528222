from django.db import models
from .ArchivedUserPreferences import ArchivedUserPreferences
from django.utils import timezone
from django.contrib.auth.models import User

class ArchivedMediaLayoutPreset(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    archive_user_id = models.ForeignKey(ArchivedUserPreferences, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    json_layout = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(auto_now_add=True)