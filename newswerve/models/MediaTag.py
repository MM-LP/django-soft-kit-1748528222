from django.db import models
from .MediaFile import MediaFile
from .Tag import Tag
from django.utils import timezone

class MediaTag(models.Model):
    media_id = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True)
    Tag_id = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
