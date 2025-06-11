
from django.db import models
from django.contrib.auth.models import User

class onboarding_event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100)  # For anonymous/guest tracking
    step = models.CharField(max_length=100)  # e.g. "Welcome", "Grant Permissions", "Create Profile"
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    duration_seconds = models.IntegerField(null=True, blank=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user or self.session_id}: {self.step} - {'✓' if self.completed else '✗'}"


