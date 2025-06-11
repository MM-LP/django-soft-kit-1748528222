from django.db import models
from django.contrib.auth.models import User

class boat_detail(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    camera_mount = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='owned_boats')

    # SurePath support
    has_surepath = models.BooleanField(default=False)
    surepath_result = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
