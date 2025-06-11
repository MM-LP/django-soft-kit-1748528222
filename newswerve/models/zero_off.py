from django.db import models

class zero_off(models.Model):
    setting = models.CharField(max_length=100, blank=True, null=True)

