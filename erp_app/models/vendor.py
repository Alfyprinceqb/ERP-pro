from django.core.validators import RegexValidator
from django.db import models

class Vendor(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Enter a valid 10-digit mobile number")]
    )
    email = models.EmailField(unique=True)    
    address = models.TextField(max_length=255, blank=True)  
