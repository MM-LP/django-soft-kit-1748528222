from django.db import models
from .contacts import contacts 

class driver_info(models.Model):
    license_number = models.CharField(max_length=50, blank=True, null=True)
    driver_name = models.ForeignKey(contacts, on_delete=models.SET_NULL, null=True)
