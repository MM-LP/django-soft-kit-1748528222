from django.db import models
from .UserPreferences import UserPreferences
from django.utils import timezone

class MediaFolder(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by_id = models.ForeignKey(UserPreferences, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)

