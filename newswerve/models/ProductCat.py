## this model is designed to create a flexible ProductInfo model. 
# ProductInfo has multiple text and number fields that have generic labelling
# The ProductCat model provides the actual labels for UI/UX

from django.db import models
from django.utils import timezone

class ProductCat(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    text1_label = models.CharField(max_length=20, blank=True, null=True)
    text2_label = models.CharField(max_length=20, blank=True, null=True)
    text3_label = models.CharField(max_length=20, blank=True, null=True)
    text4_label = models.CharField(max_length=20, blank=True, null=True)
    num1_label = models.IntegerField(blank=True, null=True)
    num2_label = models.IntegerField(blank=True, null=True)
    num3_label = models.IntegerField(blank=True, null=True)
    num4_label = models.IntegerField(blank=True, null=True)
