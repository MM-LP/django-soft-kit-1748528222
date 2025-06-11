from django.db import models
from .mobile_template import mobile_template

class template_element(models.Model):
    template = models.ForeignKey(mobile_template, on_delete=models.CASCADE, related_name='elements')
    element_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'), ('image', 'Image'), ('gif', 'GIF'), ('emoji', 'Emoji')
    ])
    content = models.TextField()
    position = models.JSONField(help_text="x, y, width, height coordinates")
    animation = models.JSONField(blank=True, null=True)
    layer = models.IntegerField(default=0)
