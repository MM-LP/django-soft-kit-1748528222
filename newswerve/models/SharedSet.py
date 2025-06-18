from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SharedSet(models.Model):
    set_id = models.CharField(max_length=100, unique=True)
    recorded_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recorded_sets')
    set_owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='owned_sets')
    is_transferred = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return f"SharedSet {self.set_id} from {self.recorded_by} to {self.set_owner}"