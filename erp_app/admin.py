from rest_framework.authtoken.models import Token
from django.contrib import admin

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass
