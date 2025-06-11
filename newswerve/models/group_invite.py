from django.db import models
from django.contrib.auth.models import User
from ski_group import ski_group

class group_invite(models.Model):
    group = models.ForeignKey(ski_group, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_invites')
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invites')
    sent_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    responded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invite to {self.invited_user.username} for group {self.group.name}