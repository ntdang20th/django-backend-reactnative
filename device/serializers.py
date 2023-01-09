from rest_framework import serializers
from device.models import *
from patient.serializers import *
from patient.models import Patient
from patient.serializers import DeviceSerializer



class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['unit_name']

class AccelerationSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    class Meta:
        model = Acceleration
        fields = ['valueX', 'valueY', 'valueZ', 'unit']

class GyroscopeSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    class Meta:
        model = Gyroscope
        fields = ['valueX', 'valueY', 'valueZ', 'unit']

class RotationSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    class Meta:
        model = Rotation
        fields = ['rotationX', 'rotationY', 'rotationZ', 'unit']

class TouchStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouchStatus
        fields = ['status_name']
        
class LocationSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    class Meta:
        model = Location
        fields = ['device', 'latitude', 'longitude', 'timestamp']

class RawdataSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    touch_status = TouchStatusSerializer(read_only=True)
    acceleration = AccelerationSerializer(read_only=True)
    gyroscope = GyroscopeSerializer(read_only=True)
    rotation = RotationSerializer(read_only=True)
    class Meta:
        model = Rawdata
        fields = ['device', 'touch_status', 'acceleration', 'gyroscope', 'rotation']