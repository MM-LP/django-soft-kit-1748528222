from django.db import models
from .skier_info import skier_info

class media_layout_preset(models.Model):
    user = models.ForeignKey(skier_info, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    json_layout = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
