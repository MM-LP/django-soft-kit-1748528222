from django.db import models
from django.contrib.auth.models import User
from .SkiGroup import SkiGroup
from django.utils import timezone

class GroupInvite(models.Model):
    group_id = models.ForeignKey(SkiGroup, on_delete=models.SET_NULL, null=True)
    invited_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_invites')
    invited_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='received_invites')
    sent_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    responded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invite to {self.invited_user.username} for group {self.group.name}"