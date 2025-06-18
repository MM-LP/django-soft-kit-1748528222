from django.db import models
from .BoatDetail import BoatDetail
from .Contacts import Contacts
from django.utils import timezone

class BoatDriver(models.Model):
    boat_id = models.ForeignKey('BoatDetail', on_delete=models.SET_NULL, null=True)
    contact_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.contact.name} - {self.boat}"