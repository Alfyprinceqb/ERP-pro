from django.db import models
from .vendor import Vendor

class Product(models.Model):
    product_id = models.CharField(max_length=255, unique=True)
    product_code = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(max_length=255)
    reorder_quantity = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')

