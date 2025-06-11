from django.db import models
from .media_file import media_file
from .skier_info import skier_info

class share_link(models.Model):
    media = models.ForeignKey(media_file, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(skier_info, on_delete=models.CASCADE)
    url = models.URLField()
    access_level = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    expiration = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
