from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArchivedContacts(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='archive_contact_info')
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    display_name = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=40, blank=True)
    address2 = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=40, blank=True)
    region = models.CharField(max_length=40, blank=True)    
    country = models.CharField(max_length=40, blank=True)
    postal_code = models.CharField(max_length=40, blank=True)

    # from swervetracker V1.0 database ---------------------------------------

    gender = models.CharField(max_length =1, blank=True)
    date_of_birth = models.DateTimeField(auto_now_add=True) 
    active = models.BooleanField(default=True, blank=False)
    newsletter = models.BooleanField(default=True, blank=True)
    app_notification = models.BooleanField(default=True, blank=False)
    feed_prompt = models.BooleanField(default=True, blank=False)
    sign_in_count = models.IntegerField(blank=True, null=True)
    #--------------------------------------------------------------------

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True) 
    is_deleted = models.BooleanField(default=False, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True) 
    archived_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
