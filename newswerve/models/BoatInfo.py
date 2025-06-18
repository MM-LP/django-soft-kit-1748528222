from django.db import models
from .BoatDetail import BoatDetail
from .Contacts import Contacts


class BoatInfo(models.Model):
    detail_id = models.ForeignKey('BoatDetail', on_delete=models.SET_NULL, null=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    owner_id = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True)
