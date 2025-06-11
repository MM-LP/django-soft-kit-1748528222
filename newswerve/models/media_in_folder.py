from django.db import models
from .media_folder import media_folder
from .media_file import media_file

class media_in_folder(models.Model):
    folder = models.ForeignKey(media_folder, on_delete=models.CASCADE)
    media = models.ForeignKey(media_file, on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, null=True)
