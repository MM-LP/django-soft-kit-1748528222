from django.db import models
from django.contrib.auth.models import User
from .Contacts import Contacts
from .ArchivedContacts import ArchivedContacts



class ArchivedTrainingDetail(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    user_id = models.ForeignKey(ArchivedContacts, on_delete=models.SET_NULL, null=True, related_name='archive_user_links')
    coach_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, related_name='archive_coach_links')
    short_desc = models.CharField(max_length=255)
    objective = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255)                   #eg. active, paused, completed
    progress = models.IntegerField(null=True, blank=True)       # %number for progress bar
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    target_fin = models.DateTimeField(auto_now_add=True)        # target finish date
    finished_at = models.DateTimeField(auto_now_add=True)
    archived_at = models.DateTimeField(auto_now_add=True)