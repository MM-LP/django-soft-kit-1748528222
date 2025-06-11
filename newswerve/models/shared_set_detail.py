from django.db import models
from django.contrib.auth.models import 
from shared_set import shared_set

class shared_set_detail(models.Model):
    shared_set = models.ForeignKey(shared_set, on_delete=models.CASCADE, related_name='details')
    event_type = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.shared_set.set_id} - {self.event_type}"