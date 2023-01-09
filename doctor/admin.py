from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_number', 'share_address', 'hospital_name']