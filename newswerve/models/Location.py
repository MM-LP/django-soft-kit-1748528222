
# -------------------- Updated Course Model with Privacy Flags --------------------

from django.db import models
from django.contrib.auth.models import User
from .Contacts import Contacts 
from django.utils import timezone

class Location(models.Model):
    # New top-level field
    name_main = models.CharField(max_length=100)  # Display/public name
    name_location = models.CharField(max_length=100)  # Formal internal name

    contact1_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses_as_contact1')
    contact1_name = models.CharField(max_length=100, blank=True)
    contact2_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses_as_contact2')
    contact2_name = models.CharField(max_length=100, blank=True)
    owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    loc_lat = models.FloatField(blank=True, null=True)
    loc_lng = models.FloatField(blank=True, null=True)

    wind_rss_url = models.URLField(blank=True)
    wind_adjust = models.IntegerField(blank=True)   #adjust wind velocity to locality (if fiarly consistent)
    wifi = models.BooleanField(default=False)
    guest_password = models.CharField(max_length=100, blank=True)
    members_only = models.BooleanField(default=False)
    facilities = models.TextField(blank=True)
    gate_code = models.CharField(max_length=50, blank=True)
    course_rules = models.FileField(upload_to='course_rules/', blank=True, null=True)
    rates = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=10, default='USD')
    notes = models.TextField(blank=True)

    # Privacy flags
    public_location = models.BooleanField(default=True)
    public_contacts = models.BooleanField(default=False)
    public_wifi = models.BooleanField(default=False)
    public_facilities = models.BooleanField(default=False)
    public_rates = models.BooleanField(default=True)
    public_course_rules = models.BooleanField(default=True)
    public_notes = models.BooleanField(default=False)

    def __str__(self):
        return self.name_main
