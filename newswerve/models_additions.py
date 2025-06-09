
from django.db import models

class MediaFile(models.Model):
    skier = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    pcloud_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    device_model = models.CharField(max_length=100, blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_lon = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MediaFolder(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MediaInFolder(models.Model):
    folder = models.ForeignKey(MediaFolder, on_delete=models.CASCADE)
    media = models.ForeignKey(MediaFile, on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, null=True)

class ShareLink(models.Model):
    media = models.ForeignKey(MediaFile, on_delete=models.CASCADE)
    shared_by = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    url = models.URLField()
    access_level = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    expiration = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Reaction(models.Model):
    media = models.ForeignKey(MediaFile, on_delete=models.CASCADE)
    user = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    type = models.CharField(max_length=20)  # like, heart, emoji, etc.
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
