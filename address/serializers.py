from rest_framework import serializers
from .models import *

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['name']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name']


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['name']


class ShareAddressSerializer(serializers.ModelSerializer):
    ward = WardSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    province = ProvinceSerializer(read_only=True)
    class Meta:
        model = ShareAddress
        fields = ['address', 'ward', 'district', 'province']