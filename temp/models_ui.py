
from django.db import models

class UISettings(models.Model):
    user = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)
    layout_style = models.CharField(max_length=50, choices=[('grid', 'Grid'), ('list', 'List')], default='grid')
    sidebar_collapsed = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class MediaTag(models.Model):
    media = models.ForeignKey('MediaFile', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class MediaLayoutPreset(models.Model):
    user = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    json_layout = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class UIEventLog(models.Model):
    user = models.ForeignKey('SkierInfo', on_delete=models.SET_NULL, null=True)
    event_type = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
