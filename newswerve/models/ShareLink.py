from django.db import models
from .MediaFile import MediaFile
from .UserPreferences import UserPreferences
from django.utils import timezone

class ShareLink(models.Model):
    media_id = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True)
    shared_by_id = models.ForeignKey(UserPreferences, on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    access_level = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    expiration = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)