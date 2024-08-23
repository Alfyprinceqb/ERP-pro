from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    role_id = models.CharField(
        max_length=255,
        choices=[
            ('admin', 'Admin'),
            ('supplier', 'Supplier'),
            ('salesperson', 'Salesperson'),
            ('customer', 'Customer')
        ]
    )
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Enter a valid 10-digit mobile number")]
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    registered_at = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    introduction = models.TextField(max_length=255, blank=True)
    address = models.TextField(max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role_id']

    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.pk is None or not self._state.adding:
            original = User.objects.filter(pk=self.pk).first()
            if original and original.password != self.password:
                self.set_password(self.password)
        else:
            self.set_password(self.password)
        super().save(*args, **kwargs)


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

class Product_category(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=255, unique=True) 
    product_code = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(max_length=255)
    product_category = models.CharField(max_length=255)
    reorder_quantity = models.IntegerField()    