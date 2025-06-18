from django.db import models
from django.contrib.auth.models import User

class ActiveContactsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)