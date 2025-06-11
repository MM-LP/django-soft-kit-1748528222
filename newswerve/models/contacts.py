from django.db import models
from django.contrib.auth.models import User

class contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    skier = models.BooleanField(default=False)
    boat_owner = models.BooleanField(default=False)
    driver = models.BooleanField(default=False)
    coach = models.BooleanField(default=False)
    course_owner = models.BooleanField(default=False)

    # Avatar and new pictures
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    pic1 = models.ImageField(upload_to='contacts/', blank=True, null=True)
    pic2 = models.ImageField(upload_to='contacts/', blank=True, null=True)
    pic3 = models.ImageField(upload_to='contacts/', blank=True, null=True)

    def __str__(self):
        return self.name
