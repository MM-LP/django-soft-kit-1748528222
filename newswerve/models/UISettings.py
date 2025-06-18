
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UISettings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dark_mode = models.BooleanField(default=False)
    layout_style = models.CharField(max_length=50, choices=[('grid', 'Grid'), ('list', 'List')], default='grid')
    sidebar_collapsed = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)
