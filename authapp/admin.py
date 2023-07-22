from django.contrib import admin

from authapp import models

# Register your models here.

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'is_active', 'date_joined']
    list_editable = ['username', 'first_name', 'last_name', 'is_active']
    ordering = ["-date_joined"]