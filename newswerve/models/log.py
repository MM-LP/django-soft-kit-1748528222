from django.db import models

class log(models.Model):
    file = models.TextField(max_length=100, blank=True, null=True)
    log_level = models.IntegerField(null=True, blank=True)
