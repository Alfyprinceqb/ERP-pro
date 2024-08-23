from django.db import models

class Product_category(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=255, unique=True) 
    product_code = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(max_length=255)
    product_category = models.CharField(max_length=255)
    reorder_quantity = models.IntegerField()
