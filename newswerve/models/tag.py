from django.db import models

class tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
