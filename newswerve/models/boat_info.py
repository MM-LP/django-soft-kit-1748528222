from django.db import models
from .boat_detail import boat_detail
from .contacts import contacts


class boat_info(models.Model):
    detail = models.ForeignKey('boat_detail', on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(contacts, on_delete=models.SET_NULL, null=True)
