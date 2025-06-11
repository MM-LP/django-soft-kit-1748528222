
from django.db import models
from django.contrib.auth.models import User

class ui_settings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)
    layout_style = models.CharField(max_length=50, choices=[('grid', 'Grid'), ('list', 'List')], default='grid')
    sidebar_collapsed = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
