from django.db import models

class speed(models.Model):
    kmph = models.FloatField(blank=True, null=True)
