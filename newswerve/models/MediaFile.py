from django.db import models
from .UserPreferences import UserPreferences
from .SetDetail import SetDetail
from django.utils import timezone

class MediaFile(models.Model):
    skier_id = models.ForeignKey(UserPreferences, on_delete=models.SET_NULL, null=True)
    pass_id = models.ForeignKey(SetDetail, on_delete=models.SET_NULL, null=True, blank=True)
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    pcloud_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    device_model = models.CharField(max_length=100, blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_lon = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
