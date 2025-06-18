from django.db import models
from django.contrib.auth.models import User
from .MediaFile import MediaFile
from .Post import Post
from django.utils import timezone

class Reaction(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    media_id = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_id = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=50)  # e.g., 'like', '🔥', '💯'


    class Meta:
        unique_together = ('post_id', 'user_id', 'type')

