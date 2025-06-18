from django.db import models
from .MediaFolder import MediaFolder
from .MediaFile import MediaFile
from django.utils import timezone

class MediaInFolder(models.Model):
    folder_id = models.ForeignKey(MediaFolder, on_delete=models.SET_NULL, null=True)
    media_id = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField(blank=True, null=True)
