
from django.db import models
from django.contrib.auth.models import User

class sync_queue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=100)
    record_id = models.CharField(max_length=100)  # Could be UUID or client-side ID
    operation = models.CharField(max_length=10, choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')])
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    synced = models.BooleanField(default=False)
    error = models.TextField(blank=True)

    def __str__(self):
        return f"{self.operation} {self.table_name} {self.record_id}"
