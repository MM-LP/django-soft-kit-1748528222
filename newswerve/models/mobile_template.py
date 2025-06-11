from django.db import models
from django.contrib.auth.models import User


class mobile_template(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    preview_image = models.ImageField(upload_to='templates/previews/', blank=True, null=True)
    base_layout = models.JSONField(help_text="JSON structure defining positioning and element layering")
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
