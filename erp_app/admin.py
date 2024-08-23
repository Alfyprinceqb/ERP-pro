from rest_framework.authtoken.models import Token
from django.contrib import admin

from django.contrib import admin
from .models import User, Vendor, Product_category

admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Product_category)

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass



