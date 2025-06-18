from django.db import models
from .Contacts import Contacts 
from django.utils import timezone

class Call(models.Model):
    contact_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True)
    call_time = models.DateTimeField(auto_now=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True)
