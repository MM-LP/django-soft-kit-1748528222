# Extended social media models for Swervetracker (Instagram-style)
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Notifications
class Notification(models.Model):
    notification_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    link_to = models.CharField(max_length=512, blank=True)  # URL or app screen ID
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
