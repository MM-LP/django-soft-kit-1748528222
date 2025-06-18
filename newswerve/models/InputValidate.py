from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class InputValidate(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    from_table = models.CharField(max_length=100)        # Name of the source table
    from_field = models.CharField(max_length=100)        # Name of the field being validated
    original = models.TextField(blank=True, null=True)   # Original free-form data
    suggested = models.TextField(blank=True, null=True)  # Admin or peer suggestion
    final = models.TextField(blank=True, null=True)      # Final accepted value
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_table}.{self.from_field} by {self.user.username if self.user else 'unknown'} [{self.status}]"
