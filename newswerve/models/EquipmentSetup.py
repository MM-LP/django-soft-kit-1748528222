from django.db import models
from .ProductInfo import ProductInfo
from django.utils import timezone

class EquipmentSetup(models.Model):

    FT_FWD_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right')
    ]

    equip_ski_id = models.ForeignKey(ProductInfo, on_delete=models.SET_NULL, null=True, related_name='ski_links')
    equip_fin_length = models.IntegerField(blank=True, null=True)
    equip_fin_depth = models.IntegerField(blank=True, null=True)
    equip_fin_DFT = models.DateTimeField(auto_now=True, null=True)
    equip_fin_leadedge = models.IntegerField(blank=True, null=True)
    equip_fin_wing = models.IntegerField(blank=True, null=True)             # wing angle
    
    equip_boot_id = models.ForeignKey(ProductInfo, on_delete=models.SET_NULL, null=True, related_name='boot_links')    
    equip_boot_position = models.IntegerField(blank=True, null=True)                      # flag for personal best
    equip_ft_fwd =models.CharField(max_length=6, choices=FT_FWD_CHOICES)
    