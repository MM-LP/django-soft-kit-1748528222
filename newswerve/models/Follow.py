from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Follow model
class Follow(models.Model):
    follower_id = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE, null=True)
    following_id = models.ForeignKey(User, related_name='followers', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)

    class Meta:
        unique_together = ('follower_id', 'following_id')

