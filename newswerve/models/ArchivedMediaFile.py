from django.db import models
from .ArchivedUserPreferences import ArchivedUserPreferences
from .ArchivedSetDetail import ArchivedSetDetail
from django.contrib.auth.models import User

class ArchivedMediaFile(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='archive_user')  
    archive_skier_id = models.ForeignKey(ArchivedUserPreferences, on_delete=models.SET_NULL, null=True, related_name='archive_skier_id')
    archive_pass_id = models.ForeignKey(ArchivedSetDetail, on_delete=models.SET_NULL, null=True, blank=True)
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    pcloud_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    device_model = models.CharField(max_length=100, blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_lon = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    archived_at = models.DateTimeField(auto_now_add=True)