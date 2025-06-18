# Extended social media models for Swervetracker (Instagram-style)
from django.db import models
from django.contrib.auth.models import User
from .ArchivedSetLog import ArchivedSetLog
from django.utils import timezone

# Post model (shared set + media)
class ArchivedPost(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    archive_setlog_id = models.ForeignKey('ArchivedSetLog', on_delete=models.SET_NULL, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(auto_now_add=True)