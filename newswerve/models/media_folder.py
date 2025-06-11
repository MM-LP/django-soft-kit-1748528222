from django.db import models
from .skier_info import skier_info

class media_folder(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(skier_info, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
