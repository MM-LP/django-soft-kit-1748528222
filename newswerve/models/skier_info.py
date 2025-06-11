from django.db import models
from .rope import rope
from .ski_detail import ski_detail
from .speed import speed
from .zero_off import zero_off

class skier_info(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    rope = models.ForeignKey(rope, on_delete=models.SET_NULL, null=True)
    ski = models.ForeignKey(ski_detail, on_delete=models.SET_NULL, null=True)
    speed = models.ForeignKey(speed, on_delete=models.SET_NULL, null=True)
    zerooff = models.ForeignKey(zero_off, on_delete=models.SET_NULL, null=True)
    partner_id = models.IntegerField(null=True, blank=True)
    children_id = models.IntegerField(null=True, blank=True)
