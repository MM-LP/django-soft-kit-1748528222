from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ArchivedTag(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=50, unique=True)
    archived_at = models.DateTimeField(auto_now_add=True)