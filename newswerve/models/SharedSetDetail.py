from django.db import models
from .SharedSet import SharedSet
from django.utils import timezone

class SharedSetDetail(models.Model):
    SharedSet_id = models.ForeignKey(SharedSet, on_delete=models.SET_NULL, null=True, related_name='details')
    event_type = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.SharedSet.set_id} - {self.event_type}"