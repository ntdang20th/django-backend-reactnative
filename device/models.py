

from django.db import models
import datetime
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from patient.models import Device
from rest_framework.renderers import JSONRenderer
# from .serializers import RawdataSerializer


#---------------------------------unit - sensor - datasending-------------------------
class Unit(models.Model):
    unit_name = models.CharField(default='', max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.unit_name

class Acceleration(models.Model):
    valueX = models.FloatField(default=0)
    valueY = models.FloatField(default=0)
    valueZ = models.FloatField(default=0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

class Gyroscope(models.Model):
    valueX = models.FloatField(default=0)
    valueY = models.FloatField(default=0)
    valueZ = models.FloatField(default=0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

class Rotation(models.Model):
    rotationX = models.FloatField(default=0)
    rotationY = models.FloatField(default=0)
    rotationZ = models.FloatField(default=0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

class TouchStatus(models.Model):
    status_name = models.CharField(default='', max_length=50)
    description = models.TextField(default='', max_length=200)

    def __str__(self):
        return self.status_name
    
class Location(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    timestamp = models.CharField(default="", max_length=30)


class Rawdata(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    touch_status = models.ForeignKey(TouchStatus, on_delete=models.CASCADE)
    acceleration = models.ForeignKey(Acceleration, on_delete=models.CASCADE)
    gyroscope = models.ForeignKey(Gyroscope, on_delete=models.CASCADE)
    rotation = models.ForeignKey(Rotation, on_delete=models.CASCADE)



