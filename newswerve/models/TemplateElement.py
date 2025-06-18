from django.db import models
from .MobileTemplate import MobileTemplate
from django.utils import timezone

class TemplateElement(models.Model):
    template_id = models.ForeignKey(MobileTemplate, on_delete=models.SET_NULL, null=True, related_name='elements')
    element_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'), ('image', 'Image'), ('gif', 'GIF'), ('emoji', 'Emoji')
    ])
    content = models.TextField()
    position = models.JSONField(help_text="x, y, width, height coordinates")
    animation = models.JSONField(blank=True, null=True)
    layer = models.IntegerField(default=0)
