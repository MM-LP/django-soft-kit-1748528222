from django.db import models
from .rope import rope

class rope_detail(models.Model):
    rope = models.ForeignKey(rope, on_delete=models.CASCADE)
    section_length = models.FloatField(blank=True, null=True)
    section_color = models.CharField(max_length=50, blank=True, null=True)
