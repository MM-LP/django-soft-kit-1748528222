
from django.db import models
from django.contrib.auth.models import User
from .mobile_detail import mobile_detail

class mobile_permission_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.ForeignKey(mobile_detail, on_delete=models.CASCADE)

    # What the user has granted access to
    allow_location = models.BooleanField(default=False)
    allow_microphone = models.BooleanField(default=False)
    allow_camera = models.BooleanField(default=False)
    allow_nfc = models.BooleanField(default=False)
    allow_wifi_status = models.BooleanField(default=False)
    allow_battery_status = models.BooleanField(default=False)
    allow_motion = models.BooleanField(default=False)

    granted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Permissions for {self.user.username} on {self.mobile}"
