from django.db import models

class ZeroOff(models.Model):
    setting = models.CharField(max_length=100, blank=True, null=True)

