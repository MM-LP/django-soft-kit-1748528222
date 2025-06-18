from django.db import models
from django.contrib.auth.models import User
from .Post import Post
class PostTag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    tagged_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)