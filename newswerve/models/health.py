
from django.db import models
from .contacts import contacts 

class health(models.Model):
    skier = models.ForeignKey('contacts', on_delete=models.CASCADE)
    injury = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    severity = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    final_status = models.CharField(max_length=100, blank=True, null=True)
    recovery_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rehab_plan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.skier} - {self.injury or 'Health Entry'}"