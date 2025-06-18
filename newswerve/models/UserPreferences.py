from django.db import models
from .Metrics import Metrics
from .ProductInfo import ProductInfo
from .Contacts import Contacts
from django.contrib.auth.models import User
from django.utils import timezone

class UserPreferences(models.Model):
    user_zerooff_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='preferences')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    age_range = models.IntegerField(null=True, blank=True)
    user_rope_id = models.ForeignKey(Metrics, on_delete=models.SET_NULL, null=True, related_name='rope_links')
    user_ski_id = models.ForeignKey(ProductInfo, on_delete=models.SET_NULL, null=True)
    user_speed_id = models.ForeignKey(Metrics, on_delete=models.SET_NULL, null=True, related_name='speed_links')
    user_zerooff_id = models.ForeignKey(Metrics, on_delete=models.SET_NULL, null=True,related_name='zerooff_links')
    user_skier = models.BooleanField(default=False)
    user_boat_owner = models.BooleanField(default=False)
    user_driver = models.BooleanField(default=False)
    user_coach = models.BooleanField(default=False)
    user_course_owner = models.BooleanField(default=False)

    # Avatar and new pictures
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    pic1 = models.ImageField(upload_to='Contacts/', blank=True, null=True)
    pic2 = models.ImageField(upload_to='Contacts/', blank=True, null=True)
    pic3 = models.ImageField(upload_to='Contacts/', blank=True, null=True)


