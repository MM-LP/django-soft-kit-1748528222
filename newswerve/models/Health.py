
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Health(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    injury = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True) #part of the body that is injured
    severity = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, null=True)           #when injury occured
    final_status = models.CharField(max_length=100, blank=True, null=True)  #healed
    recovery_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rehab_plan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.skier} - {self.injury or 'Health Entry'}"