# Extended social media models for Swervetracker (Instagram-style)
from django.db import models
from django.contrib.auth.models import User
from .ArchivedPost import ArchivedPost
from django.utils import timezone
from .ArchivedMediaFile import ArchivedMediaFile

# Media attached to posts
class ArchivedPostMedia(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    post = models.ForeignKey(ArchivedPost, on_delete=models.CASCADE, related_name='archive_media')
    archive_media_file = models.ForeignKey(ArchivedMediaFile, on_delete=models.SET_NULL, null=True)
    file_id = models.FileField(upload_to='post_media/')
    order = models.PositiveIntegerField(default=0)
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(auto_now_add=True)