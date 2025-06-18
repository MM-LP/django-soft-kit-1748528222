
from django.db import models
from django.contrib.auth.models import User
from .MediaFile import MediaFile
from .MobileTemplate import MobileTemplate
from django.utils import timezone

class UserTemplateInstance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    media_id = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True)
    template_id = models.ForeignKey(MobileTemplate, on_delete=models.SET_NULL, null=True)
    applied_elements = models.JSONField(help_text="Final user-customized layout")
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)