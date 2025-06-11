from django.db import models
from django.contrib.auth.models import User

class shared_set(models.Model):
    set_id = models.CharField(max_length=100, unique=True)
    recorded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recorded_sets')
    set_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_sets')
    created_at = models.DateTimeField(auto_now_add=True)
    is_transferred = models.BooleanField(default=False)

    def __str__(self):
        return f"SharedSet {self.set_id} from {self.recorded_by} to {self.set_owner}"