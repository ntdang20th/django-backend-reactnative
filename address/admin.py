from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(ShareAddress)
class ShareAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'ward', 'district', 'province']