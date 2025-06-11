from django.db import models
from .boat_detail import boat_detail
from .contacts import contacts

class boat_driver(models.Model):
    boat = models.ForeignKey(boat_detail, on_delete=models.CASCADE)
    contact = models.ForeignKey(contacts, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contact.name} - {self.boat}"