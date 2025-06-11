
from django.db import models
from django.contrib.auth.models import User
from .media_file import media_file
from .mobile_template import mobile_template

class user_template_instance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(media_file, on_delete=models.CASCADE)
    template = models.ForeignKey(mobile_template, on_delete=models.SET_NULL, null=True)
    applied_elements = models.JSONField(help_text="Final user-customized layout")
    created_at = models.DateTimeField(auto_now_add=True)
