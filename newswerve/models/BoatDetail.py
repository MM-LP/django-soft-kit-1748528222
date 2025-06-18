from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BoatDetail(models.Model):
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(null=True, blank=True)
    camera_mount = models.CharField(max_length=100, blank=True)
    owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='owned_boats')

    # SurePath support
    has_surepath = models.BooleanField(default=False)
    surepath_result = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)         # ✅
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
