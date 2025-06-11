from django.db import models
from .contacts import contacts 

class call(models.Model):
    contact = models.ForeignKey(contacts, on_delete=models.CASCADE)
    call_time = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True)
