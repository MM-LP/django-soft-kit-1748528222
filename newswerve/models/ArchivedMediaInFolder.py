from django.db import models
from .ArchivedMediaFolder import ArchivedMediaFolder
from .ArchivedMediaFile import ArchivedMediaFile
from django.utils import timezone
from django.contrib.auth.models import User

class ArchivedMediaInFolder(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    archive_folder_id = models.ForeignKey(ArchivedMediaFolder, on_delete=models.SET_NULL, null=True)
    archive_media_id = models.ForeignKey(ArchivedMediaFile, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField(blank=True, null=True)
    archived_at = models.DateTimeField(auto_now_add=True)