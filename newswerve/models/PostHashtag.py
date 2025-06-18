# Extended social media models for Swervetracker (Instagram-style)
from django.db import models
from django.contrib.auth.models import User
from .Post import Post
from .Hashtag import Hashtag
from django.utils import timezone

class PostHashtag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    hashtag_id = models.ForeignKey(Hashtag, on_delete=models.CASCADE, null=True)