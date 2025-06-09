
from django.db import models
from django.contrib.auth.models import User  # Replace with 'SkierInfo' if preferred

class MobileTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    preview_image = models.ImageField(upload_to='templates/previews/', blank=True, null=True)
    base_layout = models.JSONField(help_text="JSON structure defining positioning and element layering")
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TemplateElement(models.Model):
    template = models.ForeignKey(MobileTemplate, on_delete=models.CASCADE, related_name='elements')
    element_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'), ('image', 'Image'), ('gif', 'GIF'), ('emoji', 'Emoji')
    ])
    content = models.TextField()
    position = models.JSONField(help_text="x, y, width, height coordinates")
    animation = models.JSONField(blank=True, null=True)
    layer = models.IntegerField(default=0)

class UserTemplateInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey('MediaFile', on_delete=models.CASCADE)
    template = models.ForeignKey(MobileTemplate, on_delete=models.SET_NULL, null=True)
    applied_elements = models.JSONField(help_text="Final user-customized layout")
    created_at = models.DateTimeField(auto_now_add=True)
