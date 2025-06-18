from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class DeviceSyncStatus(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    device_id = models.CharField(max_length=100)  # From local storage or IndexedDB
    last_synced = models.DateTimeField(null=True, blank=True)
    last_attempt = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[('ok', 'OK'), ('conflict', 'Conflict'), ('error', 'Error')],
        default='ok'
    )

    def __str__(self):
        return f"{self.user.username} on {self.device_id}"

