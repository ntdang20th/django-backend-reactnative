from rest_framework import  serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'phone_number', 'share_address', 'hospital_name']