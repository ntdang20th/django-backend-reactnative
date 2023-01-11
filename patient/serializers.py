from rest_framework import  serializers
from .models import *
from doctor.serializers import DoctorSerializer

from address.serializers import ShareAddressSerializer


class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'

class PatientInfoSerializer(serializers.ModelSerializer):
    share_address = ShareAddressSerializer(read_only=True)
    class Meta:
        model = PatientInfo
        fields = ['last_name', 'first_name', 'gender', 'birth', 'phone_number', 'share_address', 'profile_picture']

class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient_info = PatientInfoSerializer(read_only=True)
    class Meta:
        model = Patient
        fields = ['doctor', 'patient_info']

class HasPatientFamiliarSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    familiar = FamiliarSerializer(read_only=True)
    class Meta:
        model = HasPatientFamiliar
        fields = ['patient', 'familiar']

class DeviceSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = Device
        fields = '__all__'