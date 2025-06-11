from django.db import models
from .skier_info import skier_info

class media_file(models.Model):
    skier = models.ForeignKey(skier_info, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    pcloud_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    device_model = models.CharField(max_length=100, blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_lon = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
