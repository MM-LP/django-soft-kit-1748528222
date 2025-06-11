from django.db import models
from .media_file import media_file
from .tag import tag

class media_tag(models.Model):
    media = models.ForeignKey(media_file, on_delete=models.CASCADE)
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
