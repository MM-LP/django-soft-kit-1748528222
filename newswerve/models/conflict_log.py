from django.db import models
from django.contrib.auth.models import User

class conflict_log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=100)
    record_id = models.CharField(max_length=100)
    local_version = models.JSONField()
    server_version = models.JSONField()
    resolved_version = models.JSONField(blank=True, null=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Conflict on {self.table_name}:{self.record_id}"

