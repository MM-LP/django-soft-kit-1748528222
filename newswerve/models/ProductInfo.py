from django.db import models
from .ProductCat import ProductCat
from django.utils import timezone

class ProductInfo(models.Model):
    category_id = models.ForeignKey(ProductCat, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    submodel = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    text1 = models.CharField(max_length=50, blank=True, null=True)   #custom fields for each product, defined by ProductCat (see ProductCat table)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    num3 = models.IntegerField(blank=True, null=True)
    num4 = models.IntegerField(blank=True, null=True)

