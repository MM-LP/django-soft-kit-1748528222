from django.db import models
from .Metrics import Metrics
from .ProductInfo import ProductInfo
from django.contrib.auth.models import User
from django.utils import timezone

class ArchivedUserPreferences(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='archive_preferences')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    age_range = models.IntegerField(null=True, blank=True)
    archive_user_rope_id = models.ForeignKey(Metrics, on_delete=models.SET_NULL, null=True, related_name='archive_rope_links')
    archive_user_ski_id = models.ForeignKey(ProductInfo, on_delete=models.SET_NULL, null=True)
    archive_archive_user_speed_id = models.ForeignKey(Metrics, on_delete=models.SET_NULL, null=True, related_name='archive_speed_links')
    user_zerooff_id = models.ForeignKey(Metrics, on_delete=models.SET_NULL, null=True,related_name='archive_zerooff_links')
    user_skier = models.BooleanField(default=False)
    user_boat_owner = models.BooleanField(default=False)
    user_driver = models.BooleanField(default=False)
    user_coach = models.BooleanField(default=False)
    user_course_owner = models.BooleanField(default=False)
    archived_at = models.DateTimeField(auto_now_add=True)