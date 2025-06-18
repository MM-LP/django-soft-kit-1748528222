# Extended social media models for Swervetracker (Instagram-style)
from django.db import models
from django.contrib.auth.models import User
from .Post import Post
from django.utils import timezone

# Comments on posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)         # ✅
    updated_at = models.DateTimeField(auto_now=True, blank=False) 
    is_deleted = models.BooleanField(default=False, blank=True)

