
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SyncQueue(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    table_name = models.CharField(max_length=100)
    record_id = models.CharField(max_length=100)  # Could be UUID or client-side ID
    operation = models.CharField(max_length=10, choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')])
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    synced = models.BooleanField(default=False)
    error = models.TextField(blank=True)

    def __str__(self):
        return f"{self.operation} {self.table_name} {self.record_id}"
