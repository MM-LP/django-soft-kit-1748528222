from django.db import models
from django.contrib.auth.models import User
from .Contacts import Contacts
from django.utils import timezone

class TrainingDetail(models.Model):
    user_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, related_name='user_links')
    coach_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, related_name='coach_links')
    short_desc = models.CharField(max_length=255)
    objective = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255)                   #eg. active, paused, completed
    progress = models.IntegerField(null=True, blank=True)       # %number for progress bar
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    target_fin = models.DateTimeField(auto_now_add=True)        # target finish date
    finished_at = models.DateTimeField(auto_now_add=True)
