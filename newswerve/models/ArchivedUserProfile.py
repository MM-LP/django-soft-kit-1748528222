from django.db import models
from django.contrib.auth.models import User


class ArchivedUserProfile(models.Model):
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='archive_profile') 
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_private = models.BooleanField(default=False)
    
    # Avatar and new pictures
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    pic1 = models.ImageField(upload_to='Contacts/', blank=True, null=True) #used for personalized header pic
    pic2 = models.ImageField(upload_to='Contacts/', blank=True, null=True)
    pic3 = models.ImageField(upload_to='Contacts/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    archived_at = models.DateTimeField(auto_now_add=True)