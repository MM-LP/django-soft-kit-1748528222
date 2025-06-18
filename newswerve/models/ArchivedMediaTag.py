from django.db import models
from .ArchivedMediaFile import ArchivedMediaFile
from .ArchivedTag import ArchivedTag
from django.utils import timezone
from django.contrib.auth.models import User

class ArchivedMediaTag(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    archive_media_id = models.ForeignKey(ArchivedMediaFile, on_delete=models.SET_NULL, null=True)
    archive_Tag_id = models.ForeignKey(ArchivedTag, on_delete=models.SET_NULL, null=True)
    archived_at = models.DateTimeField(auto_now_add=True)