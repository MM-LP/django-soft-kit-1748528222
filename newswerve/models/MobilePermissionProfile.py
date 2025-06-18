
from django.db import models
from django.contrib.auth.models import User
from .MobileDetail import MobileDetail
from django.utils import timezone

class MobilePermissionProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mobile_id = models.ForeignKey(MobileDetail, on_delete=models.SET_NULL, null=True)

    # What the user has granted access to
    allow_location = models.BooleanField(default=False)
    allow_microphone = models.BooleanField(default=False)
    allow_camera = models.BooleanField(default=False)
    allow_nfc = models.BooleanField(default=False)
    allow_wifi_status = models.BooleanField(default=False)
    allow_battery_status = models.BooleanField(default=False)
    allow_motion = models.BooleanField(default=False)

    granted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Permissions for {self.user.username} on {self.mobile}"
