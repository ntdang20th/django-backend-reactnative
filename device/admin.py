

from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Unit)
class WardAdmin(admin.ModelAdmin):
    list_display = ['id', 'unit_name', 'is_active']

@admin.register(Acceleration)
class AccelerationAdmin(admin.ModelAdmin):
    list_display = ['id', 'valueX', 'valueY', 'valueZ']

@admin.register(Gyroscope)
class GyroscopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'valueX', 'valueY', 'valueZ']

@admin.register(Rotation)
class RotationAdmin(admin.ModelAdmin):
    list_display = ['id', 'rotationX', 'rotationY', 'rotationZ']

@admin.register(TouchStatus)
class TouchStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name', 'description']
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'device', 'latitude', 'longitude', 'timestamp']

@admin.register(Rawdata)
class RawdataAdmin(admin.ModelAdmin):
    list_display = ['id', 'device', 'touch_status', 'acceleration', 'gyroscope', 'rotation']