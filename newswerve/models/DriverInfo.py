from django.db import models
from .Contacts import Contacts 
from django.utils import timezone

class DriverInfo(models.Model):
    LEVEL_CHOICES = [
        ('rookie', 'Rookie'),
        ('novie', 'Novice'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
        ('professional', 'Professional Driver'),
    ]

    driver_name_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True, choices=LEVEL_CHOICES)
    cert_org = models.CharField(max_length = 100, blank=True, null=True)
    cert_lvl = models.CharField(max_length=50, blank=True, null=True)
    cert_num = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)    