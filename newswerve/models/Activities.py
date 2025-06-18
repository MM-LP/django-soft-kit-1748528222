from django.db import models
from django.utils import timezone

class Activities(models.Model):
    workout_activity = models.CharField(max_length=100, null=True, blank=True)
    workout_desc = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)         # ✅
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    is_deleted = models.BooleanField(default=False, blank=True)