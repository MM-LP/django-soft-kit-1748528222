
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class OnboardingEvent(models.Model):
    STEP_CHOICES = [
        ('download', 'App Downloaded'),
        ('guest_login', 'Guest Login'),
        ('create_profile', 'Create Profile'),
        ('record_set', 'First Set Recorded'),
        ('share_set', 'First Set Shared'),
        ('convert_account', 'Converted to Registered'),
        ('feedback', 'Provided Feedback')
    ]

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    step = models.CharField(max_length=50, choices=STEP_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.step} at {self.timestamp}"


