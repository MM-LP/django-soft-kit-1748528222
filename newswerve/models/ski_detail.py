from django.db import models

class ski_detail(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    length_cm = models.IntegerField(blank=True, null=True)
