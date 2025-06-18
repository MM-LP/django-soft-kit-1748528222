# Extended social media models for Swervetracker (Instagram-style)
from django.db import models
from django.contrib.auth.models import User
from .Post import Post
from django.utils import timezone
from .MediaFile import MediaFile

# Media attached to posts
class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='media')
    media_file = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True)
    file_id = models.FileField(upload_to='post_media/')
    order = models.PositiveIntegerField(default=0)
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
