from django.db import models
from django.contrib.auth.models import User
from .media_file import media_file
from .skier_info import skier_info

class reaction(models.Model):
    media = models.ForeignKey(media_file, on_delete=models.CASCADE)
    user = models.ForeignKey(skier_info, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
